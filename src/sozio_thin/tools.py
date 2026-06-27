from __future__ import annotations

import datetime as dt
import decimal
from dataclasses import asdict
from pathlib import Path
from typing import Any

import duckdb

from sozio_thin.catalog import Catalog
from sozio_thin.pxweb import PxWebCubeTooLarge, materialize_pxweb
from sozio_thin.reproduction import reproduction_bundle
from sozio_thin.search import LocalBM25Index, normalize_text
from sozio_thin.sources import SourceRecord, SourceRegistry
from sozio_thin.sql import execute_sql as run_sql
from sozio_thin.sql import validate_sql as check_sql


class ThinTools:
    def __init__(
        self,
        *,
        catalog: Catalog | None = None,
        registry: SourceRegistry | None = None,
    ) -> None:
        self.catalog = catalog or Catalog()
        self.registry = registry or SourceRegistry()
        self.index = LocalBM25Index(self.catalog)

    def search_resources(
        self,
        question: str,
        *,
        top_k: int = 10,
        topics: list[str] | None = None,
    ) -> dict[str, Any]:
        hits = self.index.search(question, top_k=top_k, topics=topics)
        resources: list[dict[str, Any]] = []
        for hit in hits:
            profile = self.catalog.profile(str(hit.resource["resource_id"]))
            record = self.registry.register_profile(profile)
            resources.append(
                {
                    **hit.resource,
                    "score": hit.score,
                    "matched_terms": hit.matched_terms,
                    "source": asdict(record) if record else _public_source(profile),
                }
            )
        return {
            "question": question,
            "search_engine": "local_bm25",
            "catalog_size": len(self.catalog.list_resources()),
            "returned_count": len(resources),
            "resources": resources,
        }

    def get_resource_profile(
        self,
        resource_id: str,
        *,
        selectors: list[str] | None = None,
    ) -> dict[str, Any]:
        profile = self.catalog.profile(resource_id)
        record = self.registry.register_profile(profile)
        details: dict[str, Any] = {}
        if selectors:
            for selector in selectors:
                needle = normalize_text(selector)
                matches: dict[str, Any] = {}
                for key, value in (profile.get("value_summaries") or {}).items():
                    if needle in normalize_text(key):
                        matches[str(key)] = value
                details[selector] = matches
        return {
            "resource": profile,
            "selected_details": details,
            "source": asdict(record) if record else _public_source(profile),
        }

    def get_context_bundle(
        self,
        question: str,
        *,
        resource_ids: list[str] | None = None,
        top_k: int = 8,
    ) -> dict[str, Any]:
        selected_ids = resource_ids
        search_result: dict[str, Any] | None = None
        if not selected_ids:
            search_result = self.search_resources(question, top_k=top_k)
            selected_ids = [str(item["resource_id"]) for item in search_result["resources"]]
        resources: list[dict[str, Any]] = []
        sources: list[dict[str, Any]] = []
        for resource_id in selected_ids:
            profile = self.catalog.profile(resource_id)
            record = self.registry.register_profile(profile)
            resources.append(_planning_profile(profile, record))
            if record:
                sources.append(asdict(record))
        return {
            "question": question,
            "context_type": "sozio_thin_profiles",
            "resources": resources,
            "sources": sources,
            "search": search_result,
            "sql_requirements": [
                "Use only source URLs and DuckDB readers returned in this bundle.",
                "Use source column names exactly as listed.",
                "For joins, state the grain and join keys before writing SQL.",
                "Aggregate duplicate rows to the intended grain before joining.",
                "Return one read-only DuckDB SELECT or WITH query.",
                "PXWeb resources must be materialized before SQL execution.",
            ],
        }

    def materialize_resource(
        self,
        resource_id: str,
        *,
        scope: dict[str, list[str]] | None = None,
        force: bool = False,
    ) -> dict[str, Any]:
        profile = self.catalog.profile(resource_id)
        source = profile.get("source") or {}
        if str(source.get("access_method")) != "pxweb_api":
            return {
                "status": "not_pxweb_api",
                "resource_id": resource_id,
                "message": "This resource can be read directly and does not need materialization.",
            }
        api_url = str(source.get("api_url") or source.get("source_url") or "")
        try:
            cube = materialize_pxweb(api_url, scope=scope, force=force)
        except PxWebCubeTooLarge as exc:
            return {
                "status": "too_large",
                "resource_id": resource_id,
                "cell_count": exc.cell_count,
                "cell_limit": exc.cell_limit,
                "message": str(exc),
            }
        except Exception as exc:  # noqa: BLE001
            return {
                "status": "failed",
                "resource_id": resource_id,
                "error": str(exc)[:2000],
                "exception_type": exc.__class__.__name__,
            }
        record = self.registry.register_materialized(
            profile,
            parquet_path=cube.parquet_path,
            columns=cube.columns,
            metadata={"cell_count": cube.cell_count, "scoped": cube.scoped},
        )
        return {
            "status": "materialized",
            "resource_id": resource_id,
            "source": asdict(record),
            "row_count": cube.row_count,
            "columns": cube.columns,
            "cell_count": cube.cell_count,
            "cached": cube.cached,
            "scoped": cube.scoped,
        }

    def inspect_source(
        self,
        source_handle: str,
        *,
        sample_rows: int = 5,
        distinct_columns: list[str] | None = None,
        distinct_limit: int = 20,
    ) -> dict[str, Any]:
        record = self.registry.get(source_handle)
        connection = duckdb.connect(":memory:")
        try:
            schema_rows = connection.execute(f"DESCRIBE SELECT * FROM {record.duckdb_reader}").fetchall()
            sample_result = connection.execute(
                f"SELECT * FROM {record.duckdb_reader} LIMIT {max(0, int(sample_rows))}"
            )
            sample = _rows(sample_result)
            distinct: dict[str, list[Any]] = {}
            available_columns = {str(row[0]) for row in schema_rows}
            for column in distinct_columns or []:
                if column not in available_columns:
                    raise ValueError(f"Unknown column: {column}")
                quoted = '"' + column.replace('"', '""') + '"'
                values = connection.execute(
                    f"SELECT DISTINCT {quoted} FROM {record.duckdb_reader} "
                    f"WHERE {quoted} IS NOT NULL ORDER BY 1 LIMIT {max(1, int(distinct_limit))}"
                ).fetchall()
                distinct[column] = [_json_safe(row[0]) for row in values]
        finally:
            connection.close()
        return {
            "source": asdict(record),
            "schema": [
                {"column_name": row[0], "column_type": row[1], "null": row[2]}
                for row in schema_rows
            ],
            "sample_rows": sample,
            "distinct_values": distinct,
        }

    def validate_sql(
        self,
        sql: str,
        *,
        source_handles: list[str],
    ) -> dict[str, Any]:
        sources = [self.registry.get(handle) for handle in source_handles]
        return check_sql(sql, sources)

    def execute_sql(
        self,
        sql: str,
        *,
        source_handles: list[str],
        limit: int | None = None,
    ) -> dict[str, Any]:
        sources = [self.registry.get(handle) for handle in source_handles]
        return run_sql(sql, sources, limit=limit)

    def format_reproduction_bundle(
        self,
        question: str,
        sql: str,
        *,
        source_handles: list[str],
        rows: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        sources = [self.registry.get(handle) for handle in source_handles]
        return reproduction_bundle(question=question, sql=sql, sources=sources, rows=rows)


def _planning_profile(profile: dict[str, Any], record: SourceRecord | None) -> dict[str, Any]:
    return {
        "resource_id": profile.get("resource_id"),
        "title": profile.get("title"),
        "description": profile.get("description"),
        "publisher": profile.get("publisher"),
        "source_system": profile.get("source_system"),
        "primary_topic": profile.get("primary_topic"),
        "dimensions": profile.get("dimensions") or [],
        "measures": profile.get("measures") or [],
        "columns": profile.get("columns") or [],
        "geo_levels": profile.get("geo_levels") or [],
        "years": profile.get("years") or [],
        "units": profile.get("units") or [],
        "value_summaries": profile.get("value_summaries") or {},
        "pxweb_dimensions": profile.get("pxweb_dimensions") or [],
        "join_keys": profile.get("join_keys") or [],
        "semantic_warnings": profile.get("semantic_warnings") or [],
        "source": asdict(record) if record else _public_source(profile),
        "license": profile.get("license") or {},
    }


def _public_source(profile: dict[str, Any]) -> dict[str, Any]:
    source = profile.get("source") or {}
    return {
        "resource_id": profile.get("resource_id"),
        "source_url": source.get("source_url"),
        "api_url": source.get("api_url"),
        "landing_page_url": source.get("landing_page_url"),
        "format": source.get("format"),
        "access_method": source.get("access_method"),
        "materialization_required": source.get("access_method") == "pxweb_api",
    }


def _rows(result: duckdb.DuckDBPyConnection) -> list[dict[str, Any]]:
    columns = [item[0] for item in result.description or []]
    return [
        {column: _json_safe(value) for column, value in zip(columns, row, strict=False)}
        for row in result.fetchall()
    ]


def _json_safe(value: Any) -> Any:
    if isinstance(value, (dt.date, dt.datetime, dt.time, decimal.Decimal, Path)):
        return str(value)
    if isinstance(value, bytes):
        return value.hex()
    return value
