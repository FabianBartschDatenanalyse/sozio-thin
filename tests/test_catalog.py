from __future__ import annotations

import json
import sys
from pathlib import Path

from sozio_thin import catalog as catalog_module
from sozio_thin.catalog import Catalog


def test_shipped_catalog_has_exactly_100_valid_resources() -> None:
    result = Catalog().verify()
    assert result["valid"], result["issues"]
    assert result["resource_count"] == 100
    assert sum(result["topic_counts"].values()) == 100


def test_catalog_has_twenty_documented_join_pairs() -> None:
    root = Path(__file__).resolve().parents[1]
    payload = json.loads((root / "catalog" / "joins.json").read_text(encoding="utf-8"))
    assert payload["join_pair_count"] >= 20
    assert all(pair["join_keys"] for pair in payload["pairs"])


def test_catalog_contains_no_secret_or_runtime_dependency() -> None:
    root = Path(__file__).resolve().parents[1]
    text = "\n".join(path.read_text(encoding="utf-8") for path in (root / "catalog").rglob("*.json"))
    lowered = text.lower()
    assert "api_key" not in lowered
    assert "localhost:" not in lowered
    assert "127.0.0.1" not in lowered
    assert "gemini" not in lowered
    assert "vespa_url" not in lowered


def test_ten_workflow_scenarios_include_three_joins() -> None:
    root = Path(__file__).resolve().parents[1]
    scenarios = json.loads(
        (root / "tests" / "fixtures" / "workflow_scenarios.json").read_text(encoding="utf-8")
    )
    assert len(scenarios) == 10
    assert sum(bool(item["requires_join"]) for item in scenarios) >= 3


def test_runtime_does_not_import_main_project() -> None:
    root = Path(__file__).resolve().parents[1]
    runtime = "\n".join(path.read_text(encoding="utf-8") for path in (root / "src").rglob("*.py"))
    assert "sozio_research" not in runtime


def test_frozen_product_root_uses_executable_directory(monkeypatch, tmp_path: Path) -> None:
    executable = tmp_path / "sozio-thin.exe"
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(executable))
    assert catalog_module.product_root() == tmp_path


def test_catalog_falls_back_to_bundled_profiles(tmp_path: Path) -> None:
    resource_id = "ckan:test-resource"
    profile = {
        "resource_id": resource_id,
        "title": "Bundled CKAN profile",
        "primary_topic": "test",
        "source": {"source_url": "https://example.test/data.csv"},
    }
    (tmp_path / "resources.json").write_text(
        json.dumps(
            {
                "resources": [
                    {
                        "resource_id": resource_id,
                        "profile_path": "profiles/ckan_test-resource.json",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "profiles.json").write_text(
        json.dumps({"schema_version": 1, "profiles": {resource_id: profile}}),
        encoding="utf-8",
    )

    assert Catalog(tmp_path).profile(resource_id) == profile
