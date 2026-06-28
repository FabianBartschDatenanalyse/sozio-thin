# Zeitaufwand der Spitex-Organisationen und privaten Spitex-Pflegefachpersonen, Kanton St.Gallen, seit 2015

| Feld | Wert |
|---|---|
| Thema | [Gesundheit](../topics/health.md) |
| Herausgeber | Kanton St. Gallen |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2015–2024 |
| Geografie | Canton |
| Resource ID | `ckan:zeitaufwand-der-spitex-organisationen-und-privaten-spitex-pflegefachpersonen-kanton-st-gal-2015:8677da45-c533-48c6-be0e-795b60ab40f9` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/zeitaufwand-der-spitex-organisationen-und-privaten-spitex-pflegefachpersonen-kanton-st-gal-2015) · [Direkte Datenquelle](https://daten.sg.ch/api/v2/catalog/datasets/pflegestunden-der-spitex-kanton-stgallen/exports/parquet)

## Dimensionen

- year
- provider
- provider_fullname
- service
- service_fullname
- service_type
- service_type_fullname
- age_class
- hours

## Spalten

- `year`
- `provider`
- `provider_fullname`
- `service`
- `service_fullname`
- `service_type`
- `service_type_fullname`
- `age_class`
- `hours`

## Join Keys

- `canton_code`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| age_class | 6 | 5-19, 20-64, 80+, 0-4, 65-79, div |
| hours | 10 | 7681, 25397, 93605, 4807, 149605, 106651, 526, 10901 |
| provider | 3 | 1, 2, 3 |
| provider_fullname | 3 | gemeinnützige und öffentlich-rechtliche Unternehmen, erwerbswirtschaftliche Unternehmen, selbstständige Pflegefachpersonen |
| service | 4 | klv, hwt, aup, spitex |
| service_fullname | 3 | Pflegeleistungen, Hauswirtschaftliche Leistungen, Akut- und Übergangspflege |
| service_type | 3 | b, c, a |
| service_type_fullname | 3 | Untersuchung und Behandlung, Grundpflege, Abklärung und Beratung |
| year | 10 | 2015-01-01 00:00:00, 2016-01-01 00:00:00, 2017-01-01 00:00:00, 2018-01-01 00:00:00, 2019-01-01 00:00:00, 2020-01-01 00:00:00, 2021-01-01 00:00:00, 2022-01-01 00:00:00 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/zeitaufwand-der-spitex-organisationen-und-privaten-spitex-pflegefachpersonen-kanton-st-gal-2015). Kanton St. Gallen

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:zeitaufwand-der-spitex-organisationen-und-privaten-spitex-pflegefachpersonen-kanton-st-gal-2015:8677da45-c533-48c6-be0e-795b60ab40f9` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/health.md) · [Zum Katalog](../Catalog.md)
