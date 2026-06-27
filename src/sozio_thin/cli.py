from __future__ import annotations

import argparse
import json
import sys
from typing import Any

import duckdb

from sozio_thin.catalog import Catalog, product_root, state_dir
from sozio_thin.search import LocalBM25Index
from sozio_thin.server import run_server


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="sozio-thin")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("mcp-server")
    commands.add_parser("doctor")
    verify = commands.add_parser("verify-catalog")
    verify.add_argument("--expected-count", type=int, default=100)
    search = commands.add_parser("search")
    search.add_argument("question")
    search.add_argument("--top-k", type=int, default=10)
    commands.add_parser("list-resources")
    return root


def main(argv: list[str] | None = None) -> None:
    args = parser().parse_args(argv)
    if args.command == "mcp-server":
        run_server()
        return
    catalog = Catalog()
    if args.command == "verify-catalog":
        result = catalog.verify(expected_count=args.expected_count)
        _print(result)
        if not result["valid"]:
            raise SystemExit(1)
        return
    if args.command == "doctor":
        verification = catalog.verify()
        duckdb_version = duckdb.connect(":memory:").execute("SELECT version()").fetchone()[0]
        result = {
            "status": "ok" if verification["valid"] else "failed",
            "product_root": str(product_root()),
            "state_dir": str(state_dir()),
            "duckdb_version": duckdb_version,
            "catalog": verification,
            "llm_required": False,
            "vespa_required": False,
            "docker_required": False,
        }
        _print(result)
        if result["status"] != "ok":
            raise SystemExit(1)
        return
    if args.command == "search":
        hits = LocalBM25Index(catalog).search(args.question, top_k=args.top_k)
        _print(
            {
                "question": args.question,
                "hits": [
                    {"score": hit.score, "matched_terms": hit.matched_terms, **hit.resource}
                    for hit in hits
                ],
            }
        )
        return
    if args.command == "list-resources":
        _print({"resources": catalog.list_resources()})


def _print(value: Any) -> None:
    json.dump(value, sys.stdout, ensure_ascii=False, indent=2, default=str)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
