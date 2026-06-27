from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from typing import Any

from sozio_thin.catalog import Catalog

TOKEN_RE = re.compile(r"[a-z0-9]{2,}")
STOPWORDS = {
    "ab",
    "als",
    "am",
    "auf",
    "bei",
    "der",
    "die",
    "das",
    "des",
    "ein",
    "eine",
    "fur",
    "im",
    "in",
    "mit",
    "nach",
    "oder",
    "seit",
    "und",
    "von",
    "wie",
    "zu",
}
FIELD_WEIGHTS = {
    "title": 4.0,
    "description": 1.5,
    "topics": 2.0,
    "dimensions": 2.2,
    "measures": 2.5,
    "columns": 1.2,
    "geo_levels": 1.5,
    "years": 0.4,
    "sample_values": 0.6,
    "publisher": 0.5,
}


def normalize_text(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii")
    return " ".join(TOKEN_RE.findall(text.casefold()))


def tokens(value: Any) -> list[str]:
    return [token for token in normalize_text(value).split() if token not in STOPWORDS]


def flatten(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(f"{key} {flatten(item)}" for key, item in value.items())
    if isinstance(value, (list, tuple, set)):
        return " ".join(flatten(item) for item in value)
    return str(value or "")


@dataclass(frozen=True)
class SearchHit:
    score: float
    resource: dict[str, Any]
    matched_terms: list[str]


class LocalBM25Index:
    def __init__(self, catalog: Catalog) -> None:
        self.catalog = catalog
        self.documents = catalog.list_resources()
        self.field_terms: list[dict[str, Counter[str]]] = []
        self.lengths: list[float] = []
        document_frequency: Counter[str] = Counter()
        for document in self.documents:
            fields: dict[str, Counter[str]] = {}
            present: set[str] = set()
            weighted_length = 0.0
            for field, weight in FIELD_WEIGHTS.items():
                field_tokens = tokens(flatten(document.get(field)))
                counter = Counter(field_tokens)
                fields[field] = counter
                present.update(counter)
                weighted_length += len(field_tokens) * weight
            self.field_terms.append(fields)
            self.lengths.append(weighted_length)
            document_frequency.update(present)
        count = max(1, len(self.documents))
        self.idf = {
            term: math.log(1.0 + (count - frequency + 0.5) / (frequency + 0.5))
            for term, frequency in document_frequency.items()
        }
        self.average_length = sum(self.lengths) / count if self.lengths else 1.0

    def search(
        self,
        question: str,
        *,
        top_k: int = 10,
        topics: list[str] | None = None,
    ) -> list[SearchHit]:
        query_terms = list(dict.fromkeys(tokens(question)))
        normalized_question = normalize_text(question)
        forecast_requested = any(
            term in normalized_question
            for term in ("prognos", "szenari", "vorausberechn", "zukunft")
        )
        if not query_terms:
            return []
        topic_filter = {normalize_text(topic) for topic in topics or []}
        hits: list[SearchHit] = []
        for index, document in enumerate(self.documents):
            if topic_filter:
                primary_topic = normalize_text(document.get("primary_topic"))
                if primary_topic not in topic_filter:
                    continue
            score = 0.0
            matched: list[str] = []
            length_normalizer = 1.0 - 0.75 + 0.75 * self.lengths[index] / max(self.average_length, 1.0)
            for term in query_terms:
                weighted_frequency = sum(
                    FIELD_WEIGHTS[field] * self.field_terms[index][field].get(term, 0)
                    for field in FIELD_WEIGHTS
                )
                if not weighted_frequency:
                    continue
                matched.append(term)
                score += self.idf.get(term, 0.0) * (
                    weighted_frequency * 2.2 / (weighted_frequency + 1.2 * length_normalizer)
                )
                title = normalize_text(document.get("title"))
                if term in title.split():
                    score += self.idf.get(term, 0.0) * 0.75
            if score:
                title = normalize_text(document.get("title"))
                if not forecast_requested and any(
                    term in title for term in ("prognos", "szenari", "vorausberechn")
                ):
                    score *= 0.5
                hits.append(SearchHit(round(score, 6), document, matched))
        hits.sort(key=lambda hit: (-hit.score, str(hit.resource.get("resource_id"))))
        return hits[: max(0, int(top_k))]
