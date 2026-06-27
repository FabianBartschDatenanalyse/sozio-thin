from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


def product_root() -> Path:
    configured = os.environ.get("SOZIO_THIN_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parents[2]


def catalog_dir() -> Path:
    return product_root() / "catalog"


def state_dir() -> Path:
    configured = os.environ.get("SOZIO_THIN_STATE_DIR")
    path = Path(configured).expanduser() if configured else product_root() / "state"
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


class Catalog:
    def __init__(self, path: Path | None = None) -> None:
        self.path = (path or catalog_dir()).resolve()
        manifest = self._read_json(self.path / "resources.json")
        rows = manifest.get("resources") if isinstance(manifest, dict) else None
        if not isinstance(rows, list):
            raise RuntimeError(f"Invalid catalog manifest: {self.path / 'resources.json'}")
        self.manifest = manifest
        self._summaries = {
            str(row["resource_id"]): row
            for row in rows
            if isinstance(row, dict) and row.get("resource_id")
        }
        self._profile_cache: dict[str, dict[str, Any]] = {}

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise RuntimeError(f"Missing catalog file: {path}") from exc
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSON in catalog file {path}: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"Catalog file must contain a JSON object: {path}")
        return value

    def list_resources(self) -> list[dict[str, Any]]:
        return list(self._summaries.values())

    def summary(self, resource_id: str) -> dict[str, Any]:
        try:
            return self._summaries[resource_id]
        except KeyError as exc:
            raise KeyError(f"Unknown resource_id: {resource_id}") from exc

    def profile(self, resource_id: str) -> dict[str, Any]:
        cached = self._profile_cache.get(resource_id)
        if cached is not None:
            return cached
        summary = self.summary(resource_id)
        relative_path = str(summary.get("profile_path") or "")
        if not relative_path:
            raise RuntimeError(f"Resource has no profile_path: {resource_id}")
        path = (self.path / relative_path).resolve()
        if self.path not in path.parents:
            raise RuntimeError(f"Profile path escapes catalog directory: {relative_path}")
        profile = self._read_json(path)
        if str(profile.get("resource_id")) != resource_id:
            raise RuntimeError(f"Profile resource_id mismatch: {path}")
        self._profile_cache[resource_id] = profile
        return profile

    def verify(self, *, expected_count: int = 100) -> dict[str, Any]:
        issues: list[str] = []
        rows = self.list_resources()
        if len(rows) != expected_count:
            issues.append(f"expected {expected_count} resources, found {len(rows)}")
        if len(self._summaries) != len(rows):
            issues.append("resource IDs are not unique")
        topic_counts: dict[str, int] = {}
        for row in rows:
            resource_id = str(row.get("resource_id") or "")
            try:
                profile = self.profile(resource_id)
            except Exception as exc:  # noqa: BLE001
                issues.append(f"{resource_id}: {exc}")
                continue
            topic = str(profile.get("primary_topic") or "other")
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
            source = profile.get("source") or {}
            source_url = str(source.get("source_url") or "")
            api_url = str(source.get("api_url") or "")
            if not (source_url.startswith("https://") or api_url.startswith("https://")):
                issues.append(f"{resource_id}: no public HTTPS source")
            serialized = json.dumps(profile, ensure_ascii=False)
            if "C:\\\\" in serialized or "/Users/" in serialized or "/home/" in serialized:
                issues.append(f"{resource_id}: contains a local absolute path")
        return {
            "valid": not issues,
            "resource_count": len(rows),
            "topic_counts": dict(sorted(topic_counts.items())),
            "issues": issues,
        }
