from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from sozio_thin.tools import ThinTools


def create_server(tools: ThinTools | None = None) -> FastMCP:
    active_tools = tools or ThinTools()
    server = FastMCP(
        "sozio-thin",
        instructions=(
            "Deterministic Swiss open-data tools. You, the MCP client, must interpret the question, "
            "select resources, plan joins, write SQL, review errors, and explain the result. Start with "
            "search_resources or get_context_bundle. Materialize PXWeb sources before use. Validate SQL "
            "before execution and finish with format_reproduction_bundle. The server never calls an LLM."
        ),
    )

    @server.tool()
    def search_resources(
        question: str,
        top_k: int = 10,
        topics: list[str] | None = None,
    ) -> dict[str, Any]:
        """Search the local catalog of 100 curated resources."""
        return active_tools.search_resources(question, top_k=top_k, topics=topics)

    @server.tool()
    def get_resource_profile(
        resource_id: str,
        selectors: list[str] | None = None,
    ) -> dict[str, Any]:
        """Return the complete local profile and selected value details."""
        return active_tools.get_resource_profile(resource_id, selectors=selectors)

    @server.tool()
    def get_context_bundle(
        question: str,
        resource_ids: list[str] | None = None,
        top_k: int = 8,
    ) -> dict[str, Any]:
        """Build deterministic SQL-planning context without calling an LLM."""
        return active_tools.get_context_bundle(question, resource_ids=resource_ids, top_k=top_k)

    @server.tool()
    def materialize_resource(
        resource_id: str,
        scope: dict[str, list[str]] | None = None,
        force: bool = False,
    ) -> dict[str, Any]:
        """Download a scoped PXWeb cube into the local Parquet cache."""
        return active_tools.materialize_resource(resource_id, scope=scope, force=force)

    @server.tool()
    def inspect_source(
        source_handle: str,
        sample_rows: int = 5,
        distinct_columns: list[str] | None = None,
        distinct_limit: int = 20,
    ) -> dict[str, Any]:
        """Inspect the live schema, sample rows, and selected distinct values."""
        return active_tools.inspect_source(
            source_handle,
            sample_rows=sample_rows,
            distinct_columns=distinct_columns,
            distinct_limit=distinct_limit,
        )

    @server.tool()
    def validate_sql(sql: str, source_handles: list[str]) -> dict[str, Any]:
        """Validate one read-only DuckDB query against an explicit source allowlist."""
        return active_tools.validate_sql(sql, source_handles=source_handles)

    @server.tool()
    def execute_sql(
        sql: str,
        source_handles: list[str],
        limit: int | None = None,
    ) -> dict[str, Any]:
        """Validate and execute one read-only DuckDB query."""
        return active_tools.execute_sql(sql, source_handles=source_handles, limit=limit)

    @server.tool()
    def format_reproduction_bundle(
        question: str,
        sql: str,
        source_handles: list[str],
        rows: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Format the exact sources and SQL required to reproduce an answer."""
        return active_tools.format_reproduction_bundle(
            question,
            sql,
            source_handles=source_handles,
            rows=rows,
        )

    return server


def run_server() -> None:
    create_server().run(transport="stdio")
