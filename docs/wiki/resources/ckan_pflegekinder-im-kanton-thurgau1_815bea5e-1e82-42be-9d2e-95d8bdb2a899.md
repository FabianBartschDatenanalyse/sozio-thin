# Pflegekinder im Kanton Thurgau

| Feld | Wert |
|---|---|
| Thema | [Gesundheit](../topics/health.md) |
| Herausgeber | kanton-thurgau |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2019–2025 |
| Geografie | Canton |
| Resource ID | `ckan:pflegekinder-im-kanton-thurgau1:815bea5e-1e82-42be-9d2e-95d8bdb2a899` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/pflegekinder-im-kanton-thurgau1) · [Direkte Datenquelle](https://data.tg.ch/api/v2/catalog/datasets/djs-gs-6/exports/parquet)

## Dimensionen

- jahr
- status
- alterskategorie
- geschlecht
- herkunftsort
- in_pflegefamilie
- in_heim

## Spalten

- `jahr`
- `status`
- `alterskategorie`
- `geschlecht`
- `herkunftsort`
- `in_pflegefamilie`
- `in_heim`

## Join Keys

- `canton_code`
- `age_group`
- `sex`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| alterskategorie | 4 | 0-2 Jahre, 7-14 Jahre, 3-6 Jahre, 15-18 Jahre |
| geschlecht | 2 | weiblich, männlich |
| herkunftsort | 2 | Kanton Thurgau, ausserkantonal |
| in_heim | 10 | 1, 15, 3, 2, 0, 6, 4, 11 |
| in_pflegefamilie | 10 | 3, 27, 5, 4, 16, 0, 13, 28 |
| jahr | 7 | 2019-01-01 00:00:00, 2020-01-01 00:00:00, 2021-01-01 00:00:00, 2022-01-01 00:00:00, 2023-01-01 00:00:00, 2024-01-01 00:00:00, 2025-01-01 00:00:00 |
| status | 1 | Pflegekind |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/pflegekinder-im-kanton-thurgau1). kanton-thurgau

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:pflegekinder-im-kanton-thurgau1:815bea5e-1e82-42be-9d2e-95d8bdb2a899` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/health.md) · [Zum Katalog](../Catalog.md)
