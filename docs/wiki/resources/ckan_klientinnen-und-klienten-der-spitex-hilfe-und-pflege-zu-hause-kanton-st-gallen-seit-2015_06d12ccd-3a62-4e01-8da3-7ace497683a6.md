# Klientinnen und Klienten der Spitex (Hilfe und Pflege zu Hause), Kanton St.Gallen, seit 2015

| Feld | Wert |
|---|---|
| Thema | [Gesundheit](../topics/health.md) |
| Herausgeber | Kanton St. Gallen |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2015–2024 |
| Geografie | Canton |
| Resource ID | `ckan:klientinnen-und-klienten-der-spitex-hilfe-und-pflege-zu-hause-kanton-st-gallen-seit-2015:06d12ccd-3a62-4e01-8da3-7ace497683a6` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/klientinnen-und-klienten-der-spitex-hilfe-und-pflege-zu-hause-kanton-st-gallen-seit-2015) · [Direkte Datenquelle](https://daten.sg.ch/api/v2/catalog/datasets/klientinnen-und-klienten-der-spitex-kanton-stgallen/exports/parquet)

## Dimensionen

- year
- provider
- provider_fullname
- service
- service_fullname
- age_class
- sex
- anzahl

## Messgrössen

- anzahl

## Spalten

- `year`
- `provider`
- `provider_fullname`
- `service`
- `service_fullname`
- `age_class`
- `sex`
- `anzahl`

## Join Keys

- `canton_code`
- `sex`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| age_class | 5 | 0-4, 5-19, 80+, 65-79, 20-64 |
| anzahl | 10 | 0, 45, 4, 1384, 1645, 46, 616, 2 |
| provider | 3 | 1, 2, 3 |
| provider_fullname | 3 | gemeinnützige und öffentlich-rechtliche Unternehmen, erwerbswirtschaftliche Unternehmen, selbstständige Pflegefachpersonen |
| service | 3 | hwt, klv, aup |
| service_fullname | 3 | Hauswirtschaftliche Leistungen, Pflegeleistungen, Akut- und Übergangspflege |
| sex | 2 | m, f |
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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/klientinnen-und-klienten-der-spitex-hilfe-und-pflege-zu-hause-kanton-st-gallen-seit-2015). Kanton St. Gallen

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:klientinnen-und-klienten-der-spitex-hilfe-und-pflege-zu-hause-kanton-st-gallen-seit-2015:06d12ccd-3a62-4e01-8da3-7ace497683a6` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/health.md) · [Zum Katalog](../Catalog.md)
