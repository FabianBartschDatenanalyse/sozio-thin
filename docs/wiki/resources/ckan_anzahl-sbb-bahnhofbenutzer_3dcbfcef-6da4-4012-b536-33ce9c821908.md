# Number of SBB station users

| Feld | Wert |
|---|---|
| Thema | [Mobilität und Verkehr](../topics/mobility-transport.md) |
| Herausgeber | Schweizerische Bundesbahnen SBB |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2013–2025 |
| Geografie |  |
| Resource ID | `ckan:anzahl-sbb-bahnhofbenutzer:3dcbfcef-6da4-4012-b536-33ce9c821908` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/anzahl-sbb-bahnhofbenutzer) · [Direkte Datenquelle](https://data.sbb.ch/api/v2/catalog/datasets/anzahl-sbb-bahnhofbenutzer/exports/parquet)

## Dimensionen

- bahnhof_gare_stazione
- unite
- jahr
- anzahl_bahnhofbenutzer

## Messgrössen

- anzahl_bahnhofbenutzer

## Spalten

- `bahnhof_gare_stazione`
- `unite`
- `jahr`
- `anzahl_bahnhofbenutzer`

## Join Keys

- `transport_stop_id`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl_bahnhofbenutzer | 10 | 51900, 68200, 76000, 55400, 62800, 61300, 60300, 45700 |
| bahnhof_gare_stazione | 10 | Aarau, Baden, Basel SBB, Bellinzona, Bern, Biel/Bienne, Chur, Fribourg/Freiburg |
| jahr | 10 | 2021-01-01 00:00:00, 2023-01-01 00:00:00, 2013-01-01 00:00:00, 2014-01-01 00:00:00, 2019-01-01 00:00:00, 2017-01-01 00:00:00, 2018-01-01 00:00:00, 2020-01-01 00:00:00 |
| unite | 2 | DP/jour, DP/jour ouvré |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/anzahl-sbb-bahnhofbenutzer). Schweizerische Bundesbahnen SBB

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:anzahl-sbb-bahnhofbenutzer:3dcbfcef-6da4-4012-b536-33ce9c821908` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/mobility-transport.md) · [Zum Katalog](../Catalog.md)
