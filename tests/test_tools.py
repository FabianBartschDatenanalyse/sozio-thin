from __future__ import annotations

from pathlib import Path

from sozio_thin.catalog import Catalog
from sozio_thin.sources import SourceRegistry
from sozio_thin.tools import ThinTools


def tools(tmp_path: Path) -> ThinTools:
    return ThinTools(catalog=Catalog(), registry=SourceRegistry(tmp_path / "sources.json"))


def test_context_bundle_contains_planning_context_without_llm(tmp_path: Path) -> None:
    service = tools(tmp_path)
    search = service.search_resources("Arbeitsmarkt Lohn Geschlecht", top_k=2)
    ids = [item["resource_id"] for item in search["resources"]]
    bundle = service.get_context_bundle("Arbeitsmarkt Lohn Geschlecht", resource_ids=ids)
    assert bundle["context_type"] == "sozio_thin_profiles"
    assert len(bundle["resources"]) == 2
    assert all("join_keys" in resource for resource in bundle["resources"])


def test_direct_search_registers_readable_sources(tmp_path: Path) -> None:
    service = tools(tmp_path)
    result = service.search_resources("öffentliche Finanzen Steuer", top_k=10)
    direct = [item for item in result["resources"] if item["source"].get("source_handle")]
    if direct:
        assert service.registry.list()
