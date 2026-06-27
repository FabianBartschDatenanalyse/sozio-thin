from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import unicodedata
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

TOPIC_QUOTAS = {
    "population-demography": 12,
    "labor-economy": 10,
    "health": 8,
    "education": 8,
    "social-security-welfare": 8,
    "environment-energy-climate": 8,
    "mobility-transport": 8,
    "housing-construction": 6,
    "politics-elections": 6,
    "public-administration-finance": 6,
    "justice-police-safety": 5,
    "agriculture-food": 4,
    "culture-sport-tourism": 4,
    "geography-planning": 3,
    "infrastructure-utilities": 2,
    "science-research": 2,
}

TOPIC_LABELS = {
    "population-demography": "Population & Demography",
    "labor-economy": "Labor & Economy",
    "health": "Health",
    "education": "Education",
    "social-security-welfare": "Social Security & Welfare",
    "environment-energy-climate": "Environment, Energy & Climate",
    "mobility-transport": "Mobility & Transport",
    "housing-construction": "Housing & Construction",
    "politics-elections": "Politics & Elections",
    "public-administration-finance": "Public Administration & Finance",
    "justice-police-safety": "Justice, Police & Safety",
    "agriculture-food": "Agriculture & Food",
    "culture-sport-tourism": "Culture, Sport & Tourism",
    "geography-planning": "Geography & Planning",
    "infrastructure-utilities": "Infrastructure & Utilities",
    "science-research": "Science & Research",
}

TOPIC_TERMS = {
    "population-demography": {
        "bevolkerung", "demografie", "einwohner", "geburt", "sterbefall", "migration",
        "alter", "haushalt", "familie", "zivilstand", "nationalitat",
    },
    "labor-economy": {
        "arbeit", "arbeitslos", "erwerb", "beschaft", "lohn", "wirtschaft", "unternehmen",
        "branche", "bip", "preis", "konsum", "einkommen", "export", "import",
    },
    "health": {
        "gesundheit", "spital", "arzt", "arzte", "krankheit", "pflege", "medizin", "patient",
        "mortalitat", "impfung", "hospital",
    },
    "education": {
        "bildung", "schule", "schuler", "studierende", "hochschule", "universitat",
        "abschluss", "lehre", "berufsbildung", "lehrperson",
    },
    "social-security-welfare": {
        "sozial", "armut", "rent", "ahv", "iv", "invalid", "erganzungsleistung",
        "arbeitslosenversicherung", "sozialhilfe", "vorsorge", "unterstutzung", "transfer",
    },
    "environment-energy-climate": {
        "umwelt", "klima", "energie", "emission", "co2", "temperatur", "niederschlag",
        "abfall", "wasser", "luft", "biodiversitat", "strom",
    },
    "mobility-transport": {
        "verkehr", "mobilitat", "transport", "pendler", "fahrzeug", "bahn", "strasse",
        "unfall", "passagier", "reisezeit",
    },
    "housing-construction": {
        "wohnung", "wohnen", "miete", "gebaude", "bau", "immobil", "leerstand",
        "wohnflache", "hypothek",
    },
    "politics-elections": {
        "wahl", "abstimmung", "partei", "parlament", "politik", "initiative", "referendum",
        "wahlbeteiligung", "mandat",
    },
    "public-administration-finance": {
        "finanz", "steuer", "ausgabe", "einnahme", "budget", "verwaltung", "gemeindefinanz",
        "staatsrechnung", "subvention",
    },
    "justice-police-safety": {
        "kriminal", "polizei", "straftat", "verurteilung", "justiz", "gericht", "gefangnis",
        "sicherheit", "delikt", "opfer",
    },
    "agriculture-food": {
        "landwirtschaft", "betrieb", "bauern", "tier", "acker", "ernte", "lebensmittel",
        "milch", "rebe", "direktzahlung",
    },
    "culture-sport-tourism": {
        "kultur", "sport", "tourismus", "hotel", "ubernachtung", "museum", "bibliothek",
        "film", "theater", "freizeit",
    },
    "geography-planning": {
        "gemeinde", "kanton", "bezirk", "raum", "gebiet", "boden", "flache", "siedlung",
        "nutzung", "planung", "geografie",
    },
    "infrastructure-utilities": {
        "infrastruktur", "versorgung", "netz", "breitband", "telekommunikation", "wasserleitung",
        "abwasser", "post",
    },
    "science-research": {
        "forschung", "wissenschaft", "innovation", "patent", "entwicklung", "forschende",
        "technologie",
    },
}
TOPIC_PATTERNS = {
    topic: re.compile(r"\b(?:" + "|".join(re.escape(term) for term in sorted(terms)) + r")\w*")
    for topic, terms in TOPIC_TERMS.items()
}

NATIONAL_PUBLISHER_TERMS = (
    "bundesamt", "bundeskanzlei", "bfs", "meteoschweiz", "schweizerische nationalbank",
    "swissmedic", "swisstopo", "schweizerische bundesbahnen",
)

REQUIRED_CONCEPTS = {
    "labor-economy": [
        r"\blohn",
        r"\barbeitslos",
        r"\berwerb",
        r"\bbeschaft",
        r"\bunternehmen",
        r"\bbruttoinlandprodukt|\bbip\b",
        r"\bpreis",
        r"\bexport|\bimport",
        r"\beinkommen",
        r"\bbranche|\bwirtschaftssektor",
    ],
    "mobility-transport": [
        r"\bstrassenfahrzeug|\bfahrzeug",
        r"\binverkehrsetzung",
        r"\bverkehrsunfall",
        r"\bpendler",
        r"\bbahn|\bsbb",
        r"\bpassagier|\bfahrgast",
        r"\bverkehrsmittel",
        r"\bmobilitat|\btransport",
    ],
    "public-administration-finance": [
        r"\bsteuern\b|\bsteuereinnah|\bsteuerertrag|\bsteuerbelast",
        r"\boffentliche ausgaben|\bstaatsausgaben",
        r"\boffentliche einnahmen|\bstaatseinnahmen",
        r"\bfinanzen|\bfinanzrechnung",
        r"\bbudget|\bstaatsrechnung",
        r"\bverschuld|\bschulden",
    ],
}


def normalize(value: Any) -> str:
    return (
        unicodedata.normalize("NFKD", str(value or ""))
        .encode("ascii", "ignore")
        .decode("ascii")
        .casefold()
    )


def words(value: Any) -> list[str]:
    return re.findall(r"[a-z0-9]{2,}", normalize(value))


def safe_id(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", value).strip("_")[:180]


def load_raw_profiles(paths: list[Path]) -> dict[str, dict[str, Any]]:
    profiles: dict[str, dict[str, Any]] = {}
    for root in paths:
        if not root.exists():
            continue
        for path in root.rglob("*.raw_profile.json"):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            resource = payload.get("resource") or {}
            resource_id = str(resource.get("resource_id") or "")
            if resource_id and resource_id not in profiles:
                profiles[resource_id] = payload
    return profiles


def topic_scores(text: str) -> dict[str, int]:
    normalized_text = f" {normalize(text)} "
    return {
        topic: 3 * len(pattern.findall(normalized_text))
        for topic, pattern in TOPIC_PATTERNS.items()
    }


def candidate_profile(row: dict[str, Any], raw: dict[str, Any] | None) -> dict[str, Any] | None:
    resource = (raw or {}).get("resource") or {}
    raw_body = (raw or {}).get("profile") or {}
    source_row = row.get("source") or {}
    access_method = str(row.get("access_method") or resource.get("access_method") or "")
    format_name = normalize(row.get("format") or resource.get("format") or "")
    if access_method != "pxweb_api" and format_name not in {"csv", "json", "parquet", "pq"}:
        return None
    api_url = str(raw_body.get("api_url") or resource.get("api_url") or "")
    source_url = str(source_row.get("source_url") or resource.get("download_url") or "")
    if access_method == "pxweb_api":
        source_url = ""
    public_url = api_url if access_method == "pxweb_api" else source_url
    if not public_url.startswith("https://"):
        return None

    columns: list[str] = []
    dimensions: list[str] = []
    measures: list[str] = []
    years: set[int] = set()
    units: set[str] = set()
    value_summaries: dict[str, Any] = {}
    pxweb_dimensions: list[dict[str, Any]] = []
    variables = raw_body.get("variables") or []
    if variables:
        for variable in variables:
            name = str(variable.get("text") or variable.get("code") or "").strip()
            if not name:
                continue
            dimensions.append(name)
            values = list(variable.get("valueTexts") or variable.get("values") or [])
            value_summaries[name] = summarize_values(values)
            pxweb_dimensions.append(
                {
                    "code": str(variable.get("code") or ""),
                    "label": name,
                    "values": summarize_values(list(variable.get("values") or [])),
                    "value_labels": summarize_values(list(variable.get("valueTexts") or [])),
                }
            )
            if any(term in normalize(name) for term in ("statistikvariable", "kennzahl", "beobachtungseinheit")):
                measures.extend(str(value) for value in values[:30])
            if normalize(name) in {"jahr", "year", "annee", "anno"}:
                years.update(extract_years(values))
            if variable.get("unit"):
                units.add(str(variable["unit"]))
    else:
        for column in raw_body.get("columns") or []:
            name = str(column.get("name") or "").strip()
            if not name:
                continue
            columns.append(name)
            dimensions.append(name)
            values = [
                item.get("value")
                for item in (column.get("distribution") or {}).get("value_frequencies") or []
                if isinstance(item, dict)
            ] or list(column.get("sample_values") or [])
            value_summaries[name] = summarize_values(values)
            semantic = str(column.get("semantic_type") or "")
            if semantic == "year" or normalize(name) in {"jahr", "year", "periode"}:
                years.update(extract_years(values))
            if any(term in normalize(name) for term in ("anzahl", "anteil", "quote", "rate", "wert", "betrag")):
                measures.append(name)

    title = str(row.get("title") or resource.get("title") or "")
    if re.search(r"(?:^|\s+-\s+)metadaten$", normalize(title)):
        return None
    description = str(resource.get("description") or "")
    publisher = str(row.get("publisher") or resource.get("publisher") or "")
    primary_input = title
    scores = topic_scores(primary_input)
    if max(scores.values(), default=0) <= 0:
        scores = topic_scores(
            " ".join(
                [
                    primary_input,
                    description,
                    *[str(item) for item in resource.get("keywords") or []],
                    *dimensions,
                    *measures,
                ]
            )
        )
    primary_topic, primary_score = max(scores.items(), key=lambda item: (item[1], item[0]))
    if primary_score <= 0:
        return None
    topics = [topic for topic, score in scores.items() if score > 0]
    landing_page = str(resource.get("landing_page_url") or "")
    return {
        "resource_id": str(row["resource_id"]),
        "title": title,
        "description": description,
        "publisher": publisher,
        "source_system": str(row.get("source_system") or resource.get("source_system") or ""),
        "primary_topic": primary_topic,
        "topics": topics,
        "topic_score": primary_score,
        "dimensions": unique(dimensions),
        "measures": unique(measures),
        "columns": unique(columns),
        "geo_levels": infer_geo_levels(dimensions, row.get("join_keys") or []),
        "years": sorted(years),
        "units": sorted(units),
        "value_summaries": value_summaries,
        "pxweb_dimensions": pxweb_dimensions,
        "join_keys": list(row.get("join_keys") or []),
        "semantic_warnings": [],
        "source": {
            "source_url": source_url or None,
            "api_url": api_url or None,
            "landing_page_url": landing_page or None,
            "format": str(row.get("format") or resource.get("format") or ""),
            "format_family": str(row.get("format_family") or resource.get("format_family") or ""),
            "access_method": access_method,
        },
        "license": {
            "status": "verify_at_source",
            "name": "Source-specific open-data terms",
            "url": landing_page or public_url,
            "attribution": publisher,
        },
        "readiness": {
            key: bool(row.get(key))
            for key in (
                "retrievable",
                "hydrated",
                "duckdb_readable",
                "materializable",
                "join_keys_detected",
                "workflow_smoke_passed",
            )
        },
    }


def summarize_values(values: list[Any]) -> dict[str, Any]:
    clean = unique([value for value in values if value not in (None, "")])
    if len(clean) <= 25:
        return {"count": len(clean), "strategy": "full", "values": clean}
    step = max(1, math.floor(len(clean) / 10))
    sample = [clean[index] for index in range(0, len(clean), step)][:10]
    return {"count": len(clean), "strategy": "summary", "first": clean[:5], "sample": sample}


def extract_years(values: list[Any]) -> set[int]:
    result: set[int] = set()
    for value in values:
        match = re.match(r"^(19\d{2}|20\d{2})", str(value).strip())
        if match:
            result.add(int(match.group(1)))
    return result


def infer_geo_levels(dimensions: list[str], join_keys: list[str]) -> list[str]:
    text = normalize(" ".join(dimensions))
    levels: list[str] = []
    if "schweiz" in text:
        levels.append("Switzerland")
    if "kanton" in text or "canton_code" in join_keys:
        levels.append("Canton")
    if "gemeinde" in text or "bfs_municipality_id" in join_keys:
        levels.append("Municipality")
    return levels


def unique(values: list[Any]) -> list[Any]:
    seen: set[str] = set()
    result: list[Any] = []
    for value in values:
        key = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
        if key not in seen:
            seen.add(key)
            result.append(value)
    return result


def repair_text(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(repair_text(key)): repair_text(item) for key, item in value.items()}
    if isinstance(value, list):
        return [repair_text(item) for item in value]
    if not isinstance(value, str):
        return value
    repaired = value
    for _ in range(2):
        if not any(marker in repaired for marker in ("Ã", "Â", "â€", "ðŸ")):
            break
        try:
            candidate = repaired.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if candidate.count("Ã") + candidate.count("Â") >= repaired.count("Ã") + repaired.count("Â"):
            break
        repaired = candidate
    return repaired


def rank(profile: dict[str, Any]) -> tuple[int, str]:
    publisher = normalize(profile["publisher"])
    title = normalize(profile["title"])
    national = any(term in publisher for term in NATIONAL_PUBLISHER_TERMS)
    source = profile["source"]
    score = 0
    score += 100 if national else 0
    score += min(30, int(profile["topic_score"]) * 3)
    if profile["years"]:
        score += min(20, max(profile["years"]) - min(profile["years"]))
        score += 10 if max(profile["years"]) >= 2023 else 0
        score -= 30 if max(profile["years"]) < 2018 else 0
    else:
        score -= 5
    score += min(20, len(profile["join_keys"]) * 4)
    score += 15 if profile["measures"] else 0
    score += 10 if profile["geo_levels"] else 0
    score += 8 if source["access_method"] == "pxweb_api" else 10
    score += 5 if normalize(source["format"]) in {"csv", "parquet", "json"} else 0
    if any(term in title for term in ("szenari", "prognos", "vorausberechn")):
        score -= 120
    if any(term in title for term in ("city statistics", "lebensqualitat in den stadten")):
        score -= 35
    title_years = extract_years(re.findall(r"(?:19|20)\d{2}", title))
    if title_years and max(title_years) < 2018 and not profile["years"]:
        score -= 30
    return score, str(profile["resource_id"])


def family_key(profile: dict[str, Any]) -> str:
    title = normalize(profile["title"])
    title = re.sub(r"\b(?:19|20)\d{2}\b", "", title)
    title = re.split(r"\s+(?:nach|seit|ab)\s+|\s+-\s+", title, maxsplit=1)[0]
    significant = [
        token
        for token in words(title)
        if token not in {"der", "die", "das", "des", "den", "und", "von", "fur", "mit"}
    ]
    return " ".join(significant[:10])


def select(profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for profile in sorted(profiles, key=lambda item: (-rank(item)[0], rank(item)[1])):
        by_topic[profile["primary_topic"]].append(profile)

    selected: list[dict[str, Any]] = []
    seen_title: set[str] = set()
    family_counts: dict[tuple[str, str], int] = defaultdict(int)
    forecast_count = 0

    def add_candidate(profile: dict[str, Any]) -> bool:
        nonlocal forecast_count
        title_key = normalize(profile["title"])
        family = (profile["primary_topic"], family_key(profile))
        is_forecast = any(term in title_key for term in ("szenari", "prognos", "vorausberechn"))
        if title_key in seen_title or family_counts[family] >= 1:
            return False
        if is_forecast and forecast_count >= 1:
            return False
        seen_title.add(title_key)
        family_counts[family] += 1
        forecast_count += int(is_forecast)
        selected.append(profile)
        return True

    for topic, quota in TOPIC_QUOTAS.items():
        candidates = by_topic[topic]
        topic_start = len(selected)
        for pattern in REQUIRED_CONCEPTS.get(topic, []):
            for candidate in candidates:
                text = normalize(
                    " ".join(
                        [
                            candidate["title"],
                            candidate["description"],
                            *candidate["dimensions"],
                            *candidate["measures"],
                        ]
                    )
                )
                if re.search(pattern, text) and add_candidate(candidate):
                    break
        for candidate in candidates:
            if len(selected) - topic_start >= quota:
                break
            add_candidate(candidate)
        topic_count = len(selected) - topic_start
        if topic_count != quota:
            raise RuntimeError(f"Not enough diverse resources for {topic}: {topic_count} < {quota}")
    if len(selected) != 100:
        raise RuntimeError(f"Selection produced {len(selected)} resources instead of 100")
    return selected


def write_catalog(output: Path, profiles: list[dict[str, Any]], *, input_report: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    profile_dir = output / "profiles"
    profile_dir.mkdir(parents=True, exist_ok=True)
    summaries: list[dict[str, Any]] = []
    selection_rows: list[dict[str, Any]] = []
    topic_rows: dict[str, list[str]] = defaultdict(list)
    licenses: list[dict[str, Any]] = []
    desired_profile_names: set[str] = set()
    for raw_profile in sorted(profiles, key=lambda item: (item["primary_topic"], item["title"])):
        profile = repair_text(raw_profile)
        filename = f"{safe_id(profile['resource_id'])}.json"
        desired_profile_names.add(filename)
        relative = f"profiles/{filename}"
        (profile_dir / filename).write_text(
            json.dumps(profile, ensure_ascii=False, indent=2, sort_keys=True, default=str),
            encoding="utf-8",
        )
        searchable = {
            "resource_id": profile["resource_id"],
            "title": profile["title"],
            "description": profile["description"],
            "publisher": profile["publisher"],
            "source_system": profile["source_system"],
            "primary_topic": profile["primary_topic"],
            "topics": profile["topics"],
            "dimensions": profile["dimensions"],
            "measures": profile["measures"],
            "columns": profile["columns"],
            "geo_levels": profile["geo_levels"],
            "years": profile["years"],
            "sample_values": profile["value_summaries"],
            "join_keys": profile["join_keys"],
            "profile_path": relative,
        }
        summaries.append(searchable)
        topic_rows[profile["primary_topic"]].append(profile["resource_id"])
        selection_rows.append(
            {
                "resource_id": profile["resource_id"],
                "primary_topic": profile["primary_topic"],
                "selection_score": rank(profile)[0],
                "reason": "highest-ranked eligible resource within the fixed topic quota",
            }
        )
        licenses.append({"resource_id": profile["resource_id"], **profile["license"]})
    for stale_path in profile_dir.glob("*.json"):
        if stale_path.name not in desired_profile_names:
            stale_path.unlink()
    created_at = datetime.now(UTC).replace(microsecond=0).isoformat()
    write_json(
        output / "resources.json",
        {
            "catalog_version": "0.1.0",
            "created_at": created_at,
            "resource_count": len(summaries),
            "search_engine": "local_bm25",
            "resources": summaries,
        },
    )
    write_json(
        output / "topics.json",
        {
            "topics": [
                {
                    "id": topic,
                    "label": TOPIC_LABELS[topic],
                    "quota": TOPIC_QUOTAS[topic],
                    "resource_ids": sorted(topic_rows[topic]),
                }
                for topic in TOPIC_QUOTAS
            ]
        },
    )
    write_json(output / "joins.json", build_joins(profiles))
    write_json(output / "licenses.json", {"resources": licenses})
    write_json(
        output / "selection.json",
        {
            "created_at": created_at,
            "input_report": input_report.name,
            "method": "fixed topic quotas, readiness eligibility, national relevance score",
            "topic_quotas": TOPIC_QUOTAS,
            "resources": selection_rows,
        },
    )


def build_joins(profiles: list[dict[str, Any]]) -> dict[str, Any]:
    by_key: dict[str, list[str]] = defaultdict(list)
    for profile in profiles:
        for key in profile["join_keys"]:
            by_key[str(key)].append(str(profile["resource_id"]))
    pairs: list[dict[str, Any]] = []
    for key, resource_ids in sorted(by_key.items(), key=lambda item: (-len(item[1]), item[0])):
        unique_ids = sorted(set(resource_ids))
        for index in range(0, len(unique_ids) - 1, 2):
            pairs.append(
                {
                    "left_resource_id": unique_ids[index],
                    "right_resource_id": unique_ids[index + 1],
                    "join_keys": [key],
                    "warning": "Confirm grain and value coding with inspect_source before joining.",
                }
            )
            if len(pairs) >= 20:
                return {"join_pair_count": len(pairs), "pairs": pairs}
    return {"join_pair_count": len(pairs), "pairs": pairs}


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readiness-report", type=Path, required=True)
    parser.add_argument("--profile-root", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.readiness_report.read_text(encoding="utf-8"))
    raw_profiles = load_raw_profiles(args.profile_root)
    candidates: list[dict[str, Any]] = []
    for row in report.get("rows") or []:
        required = (
            row.get("retrievable")
            and row.get("hydrated")
            and row.get("materializable")
            and row.get("join_keys_detected")
            and row.get("workflow_smoke_passed")
        )
        if not required:
            continue
        profile = candidate_profile(row, raw_profiles.get(str(row.get("resource_id"))))
        if profile:
            candidates.append(profile)
    selected = select(candidates)
    write_catalog(args.output, selected, input_report=args.readiness_report)
    fingerprint = hashlib.sha256(
        "\n".join(sorted(item["resource_id"] for item in selected)).encode()
    ).hexdigest()
    print(json.dumps({"candidates": len(candidates), "selected": 100, "fingerprint": fingerprint}, indent=2))


if __name__ == "__main__":
    main()
