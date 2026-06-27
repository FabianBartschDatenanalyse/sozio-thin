from __future__ import annotations

from dataclasses import asdict
from typing import Any

from sozio_thin.sources import SourceRecord


def reproduction_bundle(
    *,
    question: str,
    sql: str,
    sources: list[SourceRecord],
    rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    source_rows = [asdict(source) for source in sources]
    lines = [
        "# Reproduction bundle",
        "",
        f"**Question:** {question}",
        "",
        "## Sources",
        "",
        "| Resource | Title | URL | Reader |",
        "|---|---|---|---|",
    ]
    for source in sources:
        lines.append(
            f"| `{_cell(source.resource_id)}` | {_cell(source.title)} | "
            f"{_cell(source.source_url)} | `{_cell(source.duckdb_reader)}` |"
        )
    lines.extend(["", "## SQL", "", "```sql", sql.strip(), "```"])
    return {
        "question": question,
        "sql": sql,
        "sources": source_rows,
        "rows_preview": list(rows or [])[:20],
        "markdown": "\n".join(lines),
    }


def _cell(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")
