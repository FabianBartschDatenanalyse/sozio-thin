# Konsolidierte Ausgaben nach funktionaler Gliederung Kanton Thurgau (Staatsrechnung)

| Feld | Wert |
|---|---|
| Thema | [Öffentliche Verwaltung und Finanzen](../topics/public-administration-finance.md) |
| Herausgeber | Kanton Thurgau |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2016–2025 |
| Geografie | Canton |
| Resource ID | `ckan:konsolidierte-ausgaben-nach-funktionaler-gliederung-kanton-thurgau-staatsrechnung:69da249e-17b1-476e-9206-2c4e0a34c72d` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/konsolidierte-ausgaben-nach-funktionaler-gliederung-kanton-thurgau-staatsrechnung) · [Direkte Datenquelle](https://data.tg.ch/api/v2/catalog/datasets/dfs-fv-10/exports/parquet)

## Dimensionen

- funktionale_gliederung
- ausgaben_millionen_chf
- jahr

## Spalten

- `funktionale_gliederung`
- `ausgaben_millionen_chf`
- `jahr`

## Join Keys

- `canton_code`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| ausgaben_millionen_chf | 10 | 225.9, 271.8, 148.5, 435.9, 381.1, 92.8, 488.2, 35.1 |
| funktionale_gliederung | 10 | Allgemeine_Verwaltung, Oeffentliche_Sicherheit, Verkehr, Gesundheit, Soziale_Wohlfahrt, Volkswirtschaft, Bildung, Kultur_Freizeit |
| jahr | 10 | 2025-01-01 00:00:00, 2024-01-01 00:00:00, 2023-01-01 00:00:00, 2022-01-01 00:00:00, 2021-01-01 00:00:00, 2020-01-01 00:00:00, 2019-01-01 00:00:00, 2018-01-01 00:00:00 |

## Workflow-Bereitschaft

| Prüfung | Status |
|---|---|
| `retrievable` | ja |
| `hydrated` | ja |
| `duckdb_readable` | ja |
| `materializable` | ja |
| `join_keys_detected` | ja |
| `workflow_smoke_passed` | ja |

## Lizenz und Attribution

[Source-specific open-data terms](https://opendata.swiss/de/dataset/konsolidierte-ausgaben-nach-funktionaler-gliederung-kanton-thurgau-staatsrechnung). Kanton Thurgau

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:konsolidierte-ausgaben-nach-funktionaler-gliederung-kanton-thurgau-staatsrechnung:69da249e-17b1-476e-9206-2c4e0a34c72d` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/public-administration-finance.md) · [Zum Katalog](../Catalog.md)
