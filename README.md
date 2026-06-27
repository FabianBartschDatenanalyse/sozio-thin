# Sozio Thin

Sozio Thin is a standalone MCP server for reproducible analysis of 100 curated
Swiss open-data resources. It runs locally without Vespa, Docker, Gemini, or an
LLM API key. The MCP client (Codex or Claude Code) performs reasoning and SQL
generation; the server only searches profiles, exposes context, materializes
PXWeb data, validates SQL, executes DuckDB, and formats reproduction details.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- Internet access when a selected public dataset must be read

The catalog contains profiles and source links, not copies of the datasets.
Version 0.1 includes PXWeb, CSV, Parquet, and JSON resources. Spreadsheets are
excluded because multi-row headers cannot be reproduced reliably by a generic
DuckDB reader.

## Setup

```powershell
cd products/sozio-thin
uv sync
uv run sozio-thin doctor
uv run sozio-thin search "Bevölkerung nach Alter und Kanton"
```

Start the stdio MCP server:

```powershell
uv run sozio-thin mcp-server
```

No environment variable is required. Runtime files are written below `state/`.
Set `SOZIO_THIN_STATE_DIR` to use another writable directory.
Slow PXWeb installations can be tuned with
`SOZIO_THIN_PXWEB_TIMEOUT_SECONDS` and `SOZIO_THIN_PXWEB_RETRY_ATTEMPTS`.

## Codex configuration

Add this server to the Codex MCP configuration, replacing the path:

```toml
[mcp_servers.sozio-thin]
command = "uv"
args = [
  "--directory",
  "C:\\path\\to\\sozio-thin",
  "run",
  "sozio-thin",
  "mcp-server",
]
```

The server uses the model already running in Codex. It cannot access or bill a
Codex subscription itself.

## Claude Code configuration

```powershell
claude mcp add sozio-thin -- uv --directory C:\path\to\sozio-thin run sozio-thin mcp-server
```

Restart the client after changing MCP configuration.

## Recommended workflow

1. Call `search_resources` for one or more parts of the research question.
2. Call `get_context_bundle` with the chosen resource IDs.
3. Materialize every selected PXWeb resource with a narrow `scope`.
4. Inspect live schemas and relevant values with `inspect_source`.
5. Formulate joins only after checking grain and key coding.
6. Call `validate_sql`, then `execute_sql`.
7. Review the returned rows in the MCP client.
8. Call `format_reproduction_bundle`.

The server deliberately has no `answer_question`, LLM review, reranking, or
literature-research tool. Those steps belong to the MCP client.

## Catalog

Every product-owned input is inspectable:

- `catalog/resources.json`: local BM25 search documents
- `catalog/profiles/*.json`: complete planning profiles
- `catalog/topics.json`: fixed topic assignments and quotas
- `catalog/joins.json`: suggested join pairs
- `catalog/licenses.json`: source attribution and license-review links
- `catalog/selection.json`: deterministic selection evidence

The source data remains governed by its publisher's terms. Verify the linked
terms before redistribution or commercial reuse.

## Catalog maintenance

The shipped catalog was generated from the full project's readiness report.
To rebuild it when those private build inputs are available:

```powershell
python scripts/select_resources.py `
  --readiness-report C:\path\to\resource_readiness_report.json `
  --profile-root C:\path\to\raw_profiles `
  --output catalog
python scripts/verify_catalog.py
```

The runtime does not need those full-project inputs.

## Tests

```powershell
uv run pytest
uv run ruff check .
```

Online source probes are marked `online` and are not part of the default unit
test run.
