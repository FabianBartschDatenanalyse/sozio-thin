# Angezeigte Straftaten nach Ausländer- und Integrationsgesetz (AIG)

| Feld | Wert |
|---|---|
| Thema | [Justiz, Polizei und Sicherheit](../topics/justice-police-safety.md) |
| Herausgeber | kanton-basel-stadt |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2009–2019 |
| Geografie | Switzerland, Municipality |
| Resource ID | `ckan:straftaten-nach-auslander-und-integrationsgesetz-aig:073a3e24-dd25-4dcf-9cfb-642d567e3dac` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/straftaten-nach-auslander-und-integrationsgesetz-aig) · [Direkte Datenquelle](https://data.bs.ch/api/v2/catalog/datasets/100441/exports/csv?use_labels=true)

## Dimensionen

- Jahr
- Gemeinde
- SR-Gesetznummer
- Gesetztitel
- Gesetztitel kurz
- Sortierung Straftat
- Straftaten
- Total Straftaten
- Aufgeklärte Straftaten
- Männliche Beschuldigte
- Weibliche Beschuldigte
- Geschlecht Beschuldigte unbekannt
- Beschuldigte Schweizer
- Beschuldigte Ausländer
- Staatsangehörigkeit Beschuldigte unbekannt
- Beschuldigte zwischen 0 und 17 Jahren
- Beschuldigte zwischen 18 und 29 Jahren
- Beschuldigte zwischen 30 und 39 Jahren
- Beschuldigte zwischen 40 und 49 Jahren
- Beschuldigte zwischen 50 und 59 Jahren
- Beschuldigte zwischen 60 und 69 Jahren
- Beschuldigte über 70 Jahren
- Alter Beschuldigte unbekannt
- Total Beschuldigte

## Spalten

- `Jahr`
- `Gemeinde`
- `SR-Gesetznummer`
- `Gesetztitel`
- `Gesetztitel kurz`
- `Sortierung Straftat`
- `Straftaten`
- `Total Straftaten`
- `Aufgeklärte Straftaten`
- `Männliche Beschuldigte`
- `Weibliche Beschuldigte`
- `Geschlecht Beschuldigte unbekannt`
- `Beschuldigte Schweizer`
- `Beschuldigte Ausländer`
- `Staatsangehörigkeit Beschuldigte unbekannt`
- `Beschuldigte zwischen 0 und 17 Jahren`
- `Beschuldigte zwischen 18 und 29 Jahren`
- `Beschuldigte zwischen 30 und 39 Jahren`
- `Beschuldigte zwischen 40 und 49 Jahren`
- `Beschuldigte zwischen 50 und 59 Jahren`
- `Beschuldigte zwischen 60 und 69 Jahren`
- `Beschuldigte über 70 Jahren`
- `Alter Beschuldigte unbekannt`
- `Total Beschuldigte`

## Join Keys

- `local_feature_id`
- `bfs_municipality_id`
- `age_group`
- `sex`
- `nationality`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| Alter Beschuldigte unbekannt | 3 | 0, 2, 1 |
| Aufgeklärte Straftaten | 10 | 111, 450, 23, 1, 2, 21, 4, 7 |
| Beschuldigte Ausländer | 10 | 92, 333, 10, 1, 25, 7, 4, 80 |
| Beschuldigte Schweizer | 10 | 0, 1, 12, 5, 6, 4, 2, 20 |
| Beschuldigte zwischen 0 und 17 Jahren | 10 | 22, 32, 0, 8, 15, 3, 23, 12 |
| Beschuldigte zwischen 18 und 29 Jahren | 10 | 34, 233, 3, 1, 16, 0, 2, 4 |
| Beschuldigte zwischen 30 und 39 Jahren | 10 | 17, 61, 2, 0, 10, 3, 18, 38 |
| Beschuldigte zwischen 40 und 49 Jahren | 10 | 12, 14, 5, 0, 9, 6, 1, 16 |
| Beschuldigte zwischen 50 und 59 Jahren | 10 | 7, 3, 0, 4, 1, 2, 5, 31 |
| Beschuldigte zwischen 60 und 69 Jahren | 10 | 2, 0, 3, 1, 9, 7, 6, 21 |
| Beschuldigte über 70 Jahren | 10 | 0, 2, 3, 1, 6, 11, 19, 22 |
| Gemeinde | 5 | Basel, Riehen, Bettingen, Gemeinde unbekannt, Kanton Basel-Stadt |
| Geschlecht Beschuldigte unbekannt | 1 | 0 |
| Gesetztitel | 1 | Ausländer- und Integrationsgesetz |
| Gesetztitel kurz | 1 | AIG |
| Jahr | 10 | 2009, 2010, 2011, 2012, 2014, 2015, 2016, 2017 |
| Männliche Beschuldigte | 10 | 74, 270, 7, 1, 22, 8, 4, 82 |
| SR-Gesetznummer | 1 | 142.2 |
| Sortierung Straftat | 10 | 11, 12, 21, 32, 40, 52, 41, 42 |
| Staatsangehörigkeit Beschuldigte unbekannt | 4 | 0, 2, 3, 1 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/straftaten-nach-auslander-und-integrationsgesetz-aig). kanton-basel-stadt

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:straftaten-nach-auslander-und-integrationsgesetz-aig:073a3e24-dd25-4dcf-9cfb-642d567e3dac` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/justice-police-safety.md) · [Zum Katalog](../Catalog.md)
