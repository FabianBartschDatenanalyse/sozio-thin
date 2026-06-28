# Öffentliche Finanzen

| Feld | Wert |
|---|---|
| Thema | [Öffentliche Verwaltung und Finanzen](../topics/public-administration-finance.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:offentliche-finanzen1:4efb0dbf-abd1-4c89-b2e9-7597cb43cdc7` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/offentliche-finanzen1) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/31646112/master)

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
- `STATUS`

## Join Keys

- `spatial_geometry`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| CLASS_HAB | 5 | Total, 2, 4, 3, 6 |
| GEOM_PERIOD | 3 | 2021-07-01, 2020-10-18, 2023-01-01 |
| GEO_NAME | 10 | Schweiz / Suisse, Affoltern am Albis, Bassersdorf, Bülach, Kloten, Opfikon, Wallisellen, Regensdorf |
| SOURCE | 2 | EFV, ESTV |
| STATUS | 3 | O, A, N |
| UNIT_VALUE | 2 | Num, Per |
| VALUE | 10 | 1309.0, 1236.0, -5.5, 1570.0, 1317.0, -16.2, 146210.66, 59718.41 |
| VALUE_PERIOD | 5 | 2021, 2019, 2020, 2019/2020, 2023 |
| VARIABLE | 10 | act_t, pat_fin_t, pat_fin_liq, pat_fin_cre, pat_fin_pla_cou, pat_fin_reg, pat_fin_sto, pat_fin_pla |
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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/offentliche-finanzen1). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:offentliche-finanzen1:4efb0dbf-abd1-4c89-b2e9-7597cb43cdc7` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/public-administration-finance.md) · [Zum Katalog](../Catalog.md)
