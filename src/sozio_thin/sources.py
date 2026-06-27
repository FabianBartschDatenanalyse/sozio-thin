from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from sozio_thin.catalog import state_dir


@dataclass
class SourceRecord:
    source_handle: str
    resource_id: str
    title: str
    source_url: str
    duckdb_reader: str
    format: str | None = None
    access_method: str | None = None
    columns: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def source_handle(resource_id: str, source_url: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", resource_id).strip("_").lower()[:70] or "source"
    digest = hashlib.sha256(f"{resource_id}\n{source_url}".encode()).hexdigest()[:10]
    return f"source:{slug}:{digest}"


def reader_for(profile: dict[str, Any], source_url: str) -> str:
    source = profile.get("source") or {}
    fmt = str(source.get("format") or "").lower()
    access_method = str(source.get("access_method") or "").lower()
    url = source_url.lower()
    literal = sql_literal(source_url)
    if access_method == "pxweb_api":
        raise ValueError("PXWeb resources must be materialized before SQL execution")
    if fmt in {"parquet", "pq"} or ".parquet" in url:
        return f"read_parquet({literal})"
    if fmt in {"json", "geojson"} or ".json" in url or ".geojson" in url:
        return f"read_json_auto({literal})"
    if fmt in {"xlsx", "xls"} or ".xlsx" in url or ".xls" in url:
        return f"read_xlsx({literal})"
    return f"read_csv_auto({literal}, ignore_errors=true)"


class SourceRegistry:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or state_dir() / "sources.json"
        self.records: dict[str, SourceRecord] = {}
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            return
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return
        for item in payload.get("sources") or []:
            try:
                record = SourceRecord(**item)
            except (TypeError, ValueError):
                continue
            self.records[record.source_handle] = record

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"sources": [asdict(record) for record in self.list()]}
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def list(self) -> list[SourceRecord]:
        return sorted(self.records.values(), key=lambda item: item.source_handle)

    def get(self, handle: str) -> SourceRecord:
        try:
            return self.records[handle]
        except KeyError as exc:
            raise KeyError(f"Unknown source_handle: {handle}") from exc

    def register_profile(
        self,
        profile: dict[str, Any],
        *,
        source_url: str | None = None,
        columns: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> SourceRecord | None:
        source = profile.get("source") or {}
        active_url = str(source_url or source.get("source_url") or "").strip()
        if not active_url or str(source.get("access_method")) == "pxweb_api":
            return None
        record = SourceRecord(
            source_handle=source_handle(str(profile["resource_id"]), active_url),
            resource_id=str(profile["resource_id"]),
            title=str(profile.get("title") or profile["resource_id"]),
            source_url=active_url,
            duckdb_reader=reader_for(profile, active_url),
            format=str(source.get("format") or "") or None,
            access_method=str(source.get("access_method") or "") or None,
            columns=list(columns or profile.get("columns") or []),
            metadata=dict(metadata or {}),
        )
        self.records[record.source_handle] = record
        self.save()
        return record

    def register_materialized(
        self,
        profile: dict[str, Any],
        *,
        parquet_path: Path,
        columns: list[str],
        metadata: dict[str, Any],
    ) -> SourceRecord:
        url = parquet_path.resolve().as_posix()
        record = SourceRecord(
            source_handle=source_handle(str(profile["resource_id"]), url),
            resource_id=str(profile["resource_id"]),
            title=str(profile.get("title") or profile["resource_id"]),
            source_url=url,
            duckdb_reader=f"read_parquet({sql_literal(url)})",
            format="parquet",
            access_method="materialized_pxweb",
            columns=columns,
            metadata=metadata,
        )
        self.records[record.source_handle] = record
        self.save()
        return record
