# Mobilität und Verkehr

| Feld | Wert |
|---|---|
| Thema | [Mobilität und Verkehr](../topics/mobility-transport.md) |
| Herausgeber | Bundesamt für Statistik BFS |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:mobilitat-und-verkehr6:bf2de1d7-68ac-4330-b2b4-5bf541c01f2d` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/mobilitat-und-verkehr6) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/24885589/master)

## Dimensionen

- ﻿"GEO_NR"
- GEO_NAME
- CLASS_HAB
- GEOM_PERIOD
- VARIABLE
- SOURCE
- VALUE_PERIOD
- UNIT_VALUE
- VALUE
- OBS_CONFIDENCE
- STATUS

## Spalten

- `﻿"GEO_NR"`
- `GEO_NAME`
- `CLASS_HAB`
- `GEOM_PERIOD`
- `VARIABLE`
- `SOURCE`
- `VALUE_PERIOD`
- `UNIT_VALUE`
- `VALUE`
- `OBS_CONFIDENCE`
- `STATUS`

## Join Keys

- `spatial_geometry`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| CLASS_HAB | 7 | Total, 2, 4, 3, 6, 5, 1 |
| GEOM_PERIOD | 2 | 2022-05-01, 2020-10-18 |
| GEO_NAME | 10 | Schweiz / Suisse, Affoltern am Albis, Bassersdorf, Bülach, Kloten, Opfikon, Wallisellen, Regensdorf |
| OBS_CONFIDENCE | 10 | 0.0, 0.4, 0.3, 7.1, 11.7, 10.3, 9.7, 5.4 |
| SOURCE | 4 | MFZ, MFZ, STATPOP, IVS, PEND, SE |
| STATUS | 1 | A |
| UNIT_VALUE | 2 | Num, Per |
| VALUE | 10 | 6339553, 4709366, 71697, 412776, 54081, 791323, 372007, 543 |
| VALUE_PERIOD | 2 | 2021, 2016/2020 |
| VARIABLE | 10 | tran_t, voit_tour, voit_tour_e, voit_livr, tran_lou, moto, tran_aut, txmot |
| ﻿"GEO_NR" | 10 | CH, 2, 52, 53, 62, 66, 69, 96 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/mobilitat-und-verkehr6). Bundesamt für Statistik BFS

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:mobilitat-und-verkehr6:bf2de1d7-68ac-4330-b2b4-5bf541c01f2d` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/mobility-transport.md) · [Zum Katalog](../Catalog.md)
