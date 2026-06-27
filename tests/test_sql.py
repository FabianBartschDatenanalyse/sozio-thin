from __future__ import annotations

from pathlib import Path

from sozio_thin.sources import SourceRecord, sql_literal
from sozio_thin.sql import execute_sql, validate_sql


def source(path: Path) -> SourceRecord:
    url = path.resolve().as_posix()
    return SourceRecord(
        source_handle="source:test",
        resource_id="test",
        title="Test",
        source_url=url,
        duckdb_reader=f"read_csv_auto({sql_literal(url)})",
        format="csv",
        access_method="download_url",
        columns=["id", "value"],
    )


def test_validate_and_execute_registered_source(tmp_path: Path) -> None:
    path = tmp_path / "values.csv"
    path.write_text("id,value\n1,10\n2,20\n", encoding="utf-8")
    record = source(path)
    sql = f"SELECT SUM(value) AS total FROM {record.duckdb_reader}"
    assert validate_sql(sql, [record])["valid"]
    result = execute_sql(sql, [record])
    assert result["status"] == "succeeded"
    assert result["rows"] == [{"total": 30}]


def test_rejects_write_operation(tmp_path: Path) -> None:
    path = tmp_path / "values.csv"
    path.write_text("id,value\n1,10\n", encoding="utf-8")
    record = source(path)
    result = validate_sql("CREATE TABLE bad AS SELECT 1", [record])
    assert not result["valid"]
    assert {issue["code"] for issue in result["issues"]} >= {"not_read_only", "forbidden_operation"}


def test_rejects_unregistered_source(tmp_path: Path) -> None:
    allowed = tmp_path / "allowed.csv"
    other = tmp_path / "other.csv"
    allowed.write_text("id\n1\n", encoding="utf-8")
    other.write_text("id\n2\n", encoding="utf-8")
    record = source(allowed)
    sql = f"SELECT * FROM read_csv_auto({sql_literal(other.resolve().as_posix())})"
    result = validate_sql(sql, [record])
    assert not result["valid"]
    assert any(issue["code"] == "source_not_allowed" for issue in result["issues"])
