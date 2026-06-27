from __future__ import annotations

import json
from pathlib import Path

from sozio_thin.catalog import Catalog
from sozio_thin.search import LocalBM25Index


def test_population_query_returns_population_resource() -> None:
    hits = LocalBM25Index(Catalog()).search("Bevölkerung Alter Geschlecht Kanton", top_k=5)
    assert hits
    assert any(hit.resource["primary_topic"] == "population-demography" for hit in hits[:3])


def test_health_query_returns_health_resource() -> None:
    hits = LocalBM25Index(Catalog()).search("Gesundheit Pflegepersonal Spital", top_k=5)
    assert hits
    assert any(hit.resource["primary_topic"] == "health" for hit in hits[:3])


def test_topic_filter_is_enforced() -> None:
    hits = LocalBM25Index(Catalog()).search(
        "Kanton Jahr",
        top_k=20,
        topics=["education"],
    )
    assert hits
    assert all(hit.resource["primary_topic"] == "education" for hit in hits)


def test_twenty_question_search_benchmark() -> None:
    path = Path(__file__).parent / "fixtures" / "search_benchmark.json"
    cases = json.loads(path.read_text(encoding="utf-8"))
    assert len(cases) == 20
    index = LocalBM25Index(Catalog())
    failures = []
    for case in cases:
        hits = index.search(case["question"], top_k=3)
        if not any(hit.resource["primary_topic"] == case["topic"] for hit in hits):
            failures.append(case)
    assert not failures
