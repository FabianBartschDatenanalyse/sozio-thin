from __future__ import annotations

import re
import time
from typing import Any

import duckdb
import sqlglot
from sqlglot import expressions as exp

from sozio_thin.sources import SourceRecord

FORBIDDEN_SQL = re.compile(
    r"\b(attach|call|copy|create|delete|detach|drop|export|import|insert|install|load|merge|pragma|"
    r"replace|set|truncate|update|vacuum)\b",
    re.IGNORECASE,
)
READER_CALL = re.compile(
    r"\b(read_csv(?:_auto)?|read_json(?:_auto)?|read_parquet|read_xlsx|st_read)\s*\(\s*'((?:''|[^'])*)'",
    re.IGNORECASE,
)


def validate_sql(sql: str, sources: list[SourceRecord]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    text = (sql or "").strip()
    if not text:
        issues.append({"code": "sql_missing", "message": "SQL must not be empty."})
        return {"valid": False, "issues": issues}
    try:
        statements = sqlglot.parse(text, read="duckdb")
    except sqlglot.errors.ParseError as exc:
        issues.append({"code": "sql_parse_failed", "message": str(exc)[:1000]})
        return {"valid": False, "issues": issues}
    if len(statements) != 1:
        issues.append({"code": "multiple_statements", "message": "Exactly one SQL statement is allowed."})
    root = statements[0] if statements else None
    if root is None or not isinstance(root, (exp.Select, exp.Union, exp.Intersect, exp.Except)):
        issues.append({"code": "not_read_only", "message": "SQL must be a read-only SELECT or WITH query."})
    if FORBIDDEN_SQL.search(text):
        issues.append({"code": "forbidden_operation", "message": "SQL contains a forbidden operation."})

    allowed_urls = {record.source_url for record in sources}
    calls = [(name.lower(), value.replace("''", "'")) for name, value in READER_CALL.findall(text)]
    if not calls:
        issues.append({"code": "source_missing", "message": "SQL must read at least one registered source."})
    for _, url in calls:
        if url not in allowed_urls:
            issues.append(
                {
                    "code": "source_not_allowed",
                    "message": "SQL references a source that was not supplied through source_handles.",
                    "source_url": url,
                }
            )
    referenced = {url for _, url in calls}
    if sources and not referenced:
        issues.append({"code": "registered_source_unused", "message": "None of the registered sources is used."})
    return {
        "valid": not issues,
        "issues": issues,
        "allowed_sources": [
            {
                "source_handle": record.source_handle,
                "resource_id": record.resource_id,
                "source_url": record.source_url,
                "duckdb_reader": record.duckdb_reader,
            }
            for record in sources
        ],
    }


def execute_sql(
    sql: str,
    sources: list[SourceRecord],
    *,
    limit: int | None = None,
) -> dict[str, Any]:
    validation = validate_sql(sql, sources)
    if not validation["valid"]:
        return {"status": "failed", "validation": validation, "rows": [], "columns": []}
    executable = sql.rstrip().rstrip(";")
    if limit is not None:
        executable = f"SELECT * FROM ({executable}) AS sozio_result LIMIT {max(0, int(limit))}"
    started = time.perf_counter()
    connection = duckdb.connect(":memory:")
    try:
        result = connection.execute(executable)
        columns = [item[0] for item in result.description or []]
        rows = [dict(zip(columns, row, strict=False)) for row in result.fetchall()]
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "failed",
            "validation": validation,
            "error": str(exc)[:2000],
            "exception_type": exc.__class__.__name__,
            "rows": [],
            "columns": [],
        }
    finally:
        connection.close()
    return {
        "status": "succeeded",
        "validation": validation,
        "execution_ms": int((time.perf_counter() - started) * 1000),
        "row_count": len(rows),
        "columns": columns,
        "rows": rows,
    }
