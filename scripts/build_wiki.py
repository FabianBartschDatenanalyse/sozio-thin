from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

TOPIC_LABELS = {
    "agriculture-food": "Landwirtschaft und Ernährung",
    "culture-sport-tourism": "Kultur, Sport und Tourismus",
    "education": "Bildung",
    "environment-energy-climate": "Umwelt, Energie und Klima",
    "geography-planning": "Geografie und Raumplanung",
    "health": "Gesundheit",
    "housing-construction": "Wohnen und Bau",
    "infrastructure-utilities": "Infrastruktur und Versorgung",
    "justice-police-safety": "Justiz, Polizei und Sicherheit",
    "labor-economy": "Arbeit und Wirtschaft",
    "mobility-transport": "Mobilität und Verkehr",
    "politics-elections": "Politik und Wahlen",
    "population-demography": "Bevölkerung und Demografie",
    "public-administration-finance": "Öffentliche Verwaltung und Finanzen",
    "science-research": "Wissenschaft und Forschung",
    "social-security-welfare": "Soziale Sicherheit",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the human-readable Sozio Thin resource wiki.")
    parser.add_argument("--catalog", type=Path, default=Path("catalog"))
    parser.add_argument("--output", type=Path, default=Path("docs/wiki"))
    args = parser.parse_args()
    result = build_wiki(args.catalog.resolve(), args.output.resolve())
    print(json.dumps(result, ensure_ascii=False))


def build_wiki(catalog_dir: Path, output_dir: Path) -> dict[str, Any]:
    if output_dir.name.lower() != "wiki" or output_dir.parent.name.lower() != "docs":
        raise RuntimeError(f"Refusing to replace a non-docs/wiki output directory: {output_dir}")
    resources_payload = _read_json(catalog_dir / "resources.json")
    topics_payload = _read_json(catalog_dir / "topics.json")
    summaries = resources_payload.get("resources")
    topics = topics_payload.get("topics")
    if not isinstance(summaries, list) or not isinstance(topics, list):
        raise RuntimeError("Catalog resources or topics are invalid")

    profiles: dict[str, dict[str, Any]] = {}
    profile_filenames: dict[str, str] = {}
    for summary in summaries:
        resource_id = str(summary["resource_id"])
        profile_path = (catalog_dir / str(summary["profile_path"])).resolve()
        if catalog_dir not in profile_path.parents:
            raise RuntimeError(f"Profile path escapes catalog: {profile_path}")
        profile = _read_json(profile_path)
        if str(profile.get("resource_id")) != resource_id:
            raise RuntimeError(f"Profile ID mismatch: {profile_path}")
        profiles[resource_id] = profile
        profile_filenames[resource_id] = f"{profile_path.stem}.md"

    topic_membership: dict[str, str] = {}
    for topic in topics:
        topic_id = str(topic["id"])
        for resource_id in topic.get("resource_ids") or []:
            topic_membership[str(resource_id)] = topic_id
    if set(profiles) != set(topic_membership):
        missing = sorted(set(profiles) - set(topic_membership))
        extra = sorted(set(topic_membership) - set(profiles))
        raise RuntimeError(f"Topic coverage mismatch. Missing={missing[:5]} extra={extra[:5]}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    (output_dir / "resources").mkdir(parents=True)
    (output_dir / "topics").mkdir()

    sorted_profiles = sorted(profiles.values(), key=lambda item: _sort_key(item.get("title")))
    _write_home(output_dir / "Home.md", topics, profiles)
    _write_home(output_dir / "README.md", topics, profiles)
    _write_topic_index(output_dir / "Topics.md", topics)
    _write_catalog(output_dir / "Catalog.md", sorted_profiles, profile_filenames)
    _write_join_index(output_dir / "Join-Keys.md", sorted_profiles, profile_filenames)
    _write_sidebar(output_dir / "_Sidebar.md", topics)

    for topic in topics:
        topic_id = str(topic["id"])
        members = [profiles[str(resource_id)] for resource_id in topic.get("resource_ids") or []]
        members.sort(key=lambda item: _sort_key(item.get("title")))
        _write_topic_page(
            output_dir / "topics" / f"{topic_id}.md",
            topic_id,
            members,
            profile_filenames,
        )

    for resource_id, profile in profiles.items():
        _write_resource_page(
            output_dir / "resources" / profile_filenames[resource_id],
            profile,
            topic_membership[resource_id],
        )

    manifest = {
        "resources": len(profiles),
        "topics": len(topics),
        "resource_pages": len(list((output_dir / "resources").glob("*.md"))),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def _write_home(
    path: Path,
    topics: list[dict[str, Any]],
    profiles: dict[str, dict[str, Any]],
) -> None:
    lines = [
        "# Sozio Thin Ressourcen-Wiki",
        "",
        (
            "Dieses Wiki macht die 100 kuratierten Schweizer Open-Data-Ressourcen "
            "des lokalen MCP-Servers für Menschen durchsuchbar."
        ),
        "",
        "## Nach Thema",
        "",
        "| Thema | Ressourcen |",
        "|---|---:|",
    ]
    for topic in topics:
        topic_id = str(topic["id"])
        label = TOPIC_LABELS.get(topic_id, str(topic.get("label") or topic_id))
        count = len(topic.get("resource_ids") or [])
        lines.append(f"| [{_md(label)}](topics/{topic_id}.md) | {count} |")
    lines.extend(
        [
            "",
            "## Weitere Einstiege",
            "",
            f"- [Alphabetischer Katalog](Catalog.md) mit {len(profiles)} Ressourcen",
            "- [Join-Key-Index](Join-Keys.md) für kombinierbare Datensätze",
            "- [GitHub-Projekt](https://github.com/FabianBartschDatenanalyse/sozio-thin)",
            "",
            "## Hinweise",
            "",
            (
                "Die Seiten beschreiben die im Produkt enthaltenen Suchprofile. Die eigentlichen Daten "
                "bleiben bei den jeweiligen Herausgebern und werden erst bei einer Analyse geladen."
            ),
            (
                "PXWeb-Ressourcen müssen mit `materialize_resource` auf einen passenden Ausschnitt "
                "begrenzt werden. Direkte CSV-, JSON- und Parquet-Quellen können unmittelbar gelesen werden."
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_topic_index(path: Path, topics: list[dict[str, Any]]) -> None:
    lines = ["# Themen", ""]
    for topic in topics:
        topic_id = str(topic["id"])
        label = TOPIC_LABELS.get(topic_id, str(topic.get("label") or topic_id))
        lines.append(f"- [{_md(label)}](topics/{topic_id}.md) ({len(topic.get('resource_ids') or [])})")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_topic_page(
    path: Path,
    topic_id: str,
    profiles: list[dict[str, Any]],
    filenames: dict[str, str],
) -> None:
    label = TOPIC_LABELS.get(topic_id, topic_id)
    lines = [
        f"# {_md(label)}",
        "",
        f"{len(profiles)} Ressourcen.",
        "",
        "| Ressource | Herausgeber | Format | Zeitraum | Join Keys |",
        "|---|---|---|---|---|",
    ]
    for profile in profiles:
        resource_id = str(profile["resource_id"])
        source = profile.get("source") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    f"[{_cell(profile.get('title'))}](../resources/{filenames[resource_id]})",
                    _cell(profile.get("publisher")),
                    _cell(source.get("format") or source.get("format_family")),
                    _cell(_years(profile.get("years"))),
                    _cell(", ".join(str(item) for item in profile.get("join_keys") or [])),
                ]
            )
            + " |"
        )
    lines.extend(["", "[Zurück zur Themenübersicht](../Topics.md)", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_catalog(
    path: Path,
    profiles: list[dict[str, Any]],
    filenames: dict[str, str],
) -> None:
    lines = [
        "# Alphabetischer Katalog",
        "",
        f"{len(profiles)} Ressourcen, sortiert nach Titel.",
        "",
    ]
    for profile in profiles:
        resource_id = str(profile["resource_id"])
        lines.append(
            f"- [{_md(profile.get('title'))}](resources/{filenames[resource_id]})"
            f" — {_md(profile.get('publisher'))}"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_join_index(
    path: Path,
    profiles: list[dict[str, Any]],
    filenames: dict[str, str],
) -> None:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for profile in profiles:
        for join_key in profile.get("join_keys") or []:
            groups[str(join_key)].append(profile)
    lines = [
        "# Join-Key-Index",
        "",
        (
            "Gemeinsame Join Keys sind Hinweise auf mögliche Verknüpfungen. Vor einem Join müssen "
            "Granularität, Codes und Mehrfachzeilen trotzdem geprüft werden."
        ),
        "",
    ]
    for join_key in sorted(groups, key=_sort_key):
        lines.extend([f"## `{join_key}`", ""])
        for profile in groups[join_key]:
            resource_id = str(profile["resource_id"])
            lines.append(f"- [{_md(profile.get('title'))}](resources/{filenames[resource_id]})")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_resource_page(path: Path, profile: dict[str, Any], topic_id: str) -> None:
    source = profile.get("source") or {}
    readiness = profile.get("readiness") or {}
    license_info = profile.get("license") or {}
    title = _md(profile.get("title"))
    lines = [
        f"# {title}",
        "",
        "| Feld | Wert |",
        "|---|---|",
        f"| Thema | [{_cell(TOPIC_LABELS.get(topic_id, topic_id))}](../topics/{topic_id}.md) |",
        f"| Herausgeber | {_cell(profile.get('publisher'))} |",
        f"| Ressourcentyp | {_cell(profile.get('source_system'))} |",
        f"| Format | {_cell(source.get('format') or source.get('format_family'))} |",
        f"| Zugriff | {_cell(source.get('access_method'))} |",
        f"| Zeitraum | {_cell(_years(profile.get('years')))} |",
        f"| Geografie | {_cell(', '.join(str(item) for item in profile.get('geo_levels') or []))} |",
        f"| Resource ID | `{_code(profile.get('resource_id'))}` |",
        "",
    ]
    description = _md(profile.get("description"))
    if description:
        lines.extend(["## Beschreibung", "", description, ""])

    source_links = []
    if source.get("landing_page_url"):
        source_links.append(f"[Datensatzseite]({source['landing_page_url']})")
    if source.get("source_url"):
        source_links.append(f"[Direkte Datenquelle]({source['source_url']})")
    if source.get("api_url"):
        source_links.append(f"[API-Endpunkt]({source['api_url']})")
    lines.extend(["## Quelle", "", " · ".join(source_links) if source_links else "Keine URL hinterlegt.", ""])

    _append_list(lines, "Dimensionen", profile.get("dimensions"))
    _append_list(lines, "Messgrössen", profile.get("measures"))
    _append_list(lines, "Spalten", profile.get("columns"), code=True)
    _append_list(lines, "Einheiten", profile.get("units"))
    _append_list(lines, "Join Keys", profile.get("join_keys"), code=True)
    _append_list(lines, "Semantische Hinweise", profile.get("semantic_warnings"))

    pxweb_dimensions = profile.get("pxweb_dimensions") or []
    if pxweb_dimensions:
        lines.extend(
            [
                "## PXWeb-Dimensionen",
                "",
                "| Code | Werte | Beispiele |",
                "|---|---:|---|",
            ]
        )
        for dimension in pxweb_dimensions:
            values = dimension.get("values") or {}
            examples = values.get("values") or values.get("first") or values.get("sample") or []
            lines.append(
                f"| `{_code(dimension.get('code'))}` | {values.get('count', '')} | "
                f"{_cell(', '.join(str(item) for item in examples[:8]))} |"
            )
        lines.append("")

    value_summaries = profile.get("value_summaries") or {}
    if value_summaries:
        lines.extend(["## Beispielwerte", "", "| Feld | Anzahl | Beispiele |", "|---|---:|---|"])
        for name, summary in list(value_summaries.items())[:20]:
            examples = summary.get("values") or summary.get("first") or summary.get("sample") or []
            lines.append(
                f"| {_cell(name)} | {summary.get('count', '')} | "
                f"{_cell(', '.join(str(item) for item in examples[:8]))} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Workflow-Bereitschaft",
            "",
            "| Prüfung | Status |",
            "|---|---|",
        ]
    )
    for key in (
        "retrievable",
        "hydrated",
        "duckdb_readable",
        "materializable",
        "join_keys_detected",
        "workflow_smoke_passed",
    ):
        lines.append(f"| `{key}` | {'ja' if readiness.get(key) else 'nein'} |")
    lines.append("")

    if license_info:
        license_text = _md(license_info.get("name") or license_info.get("status"))
        if license_info.get("url"):
            license_text = f"[{license_text}]({license_info['url']})"
        attribution = _md(license_info.get("attribution"))
        lines.extend(["## Lizenz und Attribution", "", f"{license_text}. {attribution}".strip(), ""])

    lines.extend(
        [
            "## Verwendung im MCP",
            "",
            f"1. Mit `get_resource_profile` die Resource ID `{_code(profile.get('resource_id'))}` laden.",
        ]
    )
    if source.get("access_method") == "pxweb_api":
        lines.append("2. Mit `materialize_resource` einen ausreichend kleinen PXWeb-Ausschnitt laden.")
    else:
        lines.append("2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.")
    lines.extend(
        [
            "3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.",
            "4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.",
            "",
            "[Zurück zum Thema](../topics/" + topic_id + ".md) · [Zum Katalog](../Catalog.md)",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_sidebar(path: Path, topics: list[dict[str, Any]]) -> None:
    lines = [
        "## Sozio Thin",
        "",
        "- [Start](Home.md)",
        "- [Alle Themen](Topics.md)",
        "- [Katalog](Catalog.md)",
        "- [Join Keys](Join-Keys.md)",
        "",
        "### Themen",
        "",
    ]
    for topic in topics:
        topic_id = str(topic["id"])
        label = TOPIC_LABELS.get(topic_id, topic_id)
        lines.append(f"- [{_md(label)}](topics/{topic_id}.md)")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _append_list(
    lines: list[str],
    title: str,
    values: Any,
    *,
    code: bool = False,
) -> None:
    if not isinstance(values, list) or not values:
        return
    lines.extend([f"## {title}", ""])
    for value in values:
        text = _md(value)
        lines.append(f"- `{' '.join(text.split())}`" if code else f"- {text}")
    lines.append("")


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return payload


def _years(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return ""
    years = sorted({str(item) for item in value})
    if len(years) > 2 and all(re.fullmatch(r"\d{4}", year) for year in years):
        return f"{years[0]}–{years[-1]}"
    return ", ".join(years[:12])


def _sort_key(value: Any) -> str:
    normalized = unicodedata.normalize("NFKD", str(value or ""))
    return "".join(char for char in normalized if not unicodedata.combining(char)).casefold()


def _md(value: Any) -> str:
    return " ".join(str(value or "").replace("\r", " ").replace("\n", " ").split())


def _cell(value: Any) -> str:
    return _md(value).replace("|", "\\|")


def _code(value: Any) -> str:
    return _md(value).replace("`", "'")


if __name__ == "__main__":
    main()
