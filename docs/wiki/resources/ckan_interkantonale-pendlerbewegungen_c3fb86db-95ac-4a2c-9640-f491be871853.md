# Interkantonale Pendlerbewegungen

| Feld | Wert |
|---|---|
| Thema | [Mobilität und Verkehr](../topics/mobility-transport.md) |
| Herausgeber | kanton-zug |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2010–2022 |
| Geografie | Canton |
| Resource ID | `ckan:interkantonale-pendlerbewegungen:c3fb86db-95ac-4a2c-9640-f491be871853` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/interkantonale-pendlerbewegungen) · [Direkte Datenquelle](https://data.zg.ch/store/1/resource/534)

## Dimensionen

- periode
- gebiet
- kennzahl
- anzahl

## Messgrössen

- anzahl

## Spalten

- `periode`
- `gebiet`
- `kennzahl`
- `anzahl`

## Join Keys

- `canton_code`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl | 10 | 4905, 1471, 11251, 4925, 4576, 2272, 5492, 1317 |
| gebiet | 5 | Aargau, Luzern, Restliche Schweiz, Schwyz, Zürich |
| kennzahl | 2 | Pendler nach Zug, Pendler von Zug |
| periode | 5 | 2010-2012, 2013-2015, 2016-2018, 2019-2021, 2022-2024 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/interkantonale-pendlerbewegungen). kanton-zug

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:interkantonale-pendlerbewegungen:c3fb86db-95ac-4a2c-9640-f491be871853` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/mobility-transport.md) · [Zum Katalog](../Catalog.md)
