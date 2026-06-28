# Nationalratswahlen: Zeitreihen zu Listen, Kandidierenden, Parteistärken, Mandaten, gewählten Frauen und Männern, stärkste Partei (Schweiz und Kantone)

| Feld | Wert |
|---|---|
| Thema | [Politik und Wahlen](../topics/politics-elections.md) |
| Herausgeber | Bundesamt für Statistik BFS |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 1991–2023 |
| Geografie | Canton |
| Resource ID | `ckan:nationalratswahlen-zeitreihen-zu-listen-kandidierenden-parteistarken-mandaten-gewahlten-frauen-:248576ad-1b14-4dba-b6c9-4ae0f934ea13` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/nationalratswahlen-zeitreihen-zu-listen-kandidierenden-parteistarken-mandaten-gewahlten-frauen-) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/28845369/appendix)

## Dimensionen

- wahl_jahr
- ebene_resultat
- geoLevelName
- kanton_nummer
- kanton_bezeichnung
- partei_id
- partei_bezeichnung_de
- partei_bezeichnung_fr
- partei_bezeichnung_it
- partei_bezeichnung_en
- partei_staerke
- flag_staerkste_partei
- anzahl_listen
- anzahl_kandidierende
- anzahl_kandidierende_f
- anzahl_kandidierende_m
- anzahl_gewaehlte
- anzahl_gewaehlte_f
- anzahl_gewaehlte_m
- frauen_anteil

## Messgrössen

- anzahl_listen
- anzahl_kandidierende
- anzahl_kandidierende_f
- anzahl_kandidierende_m
- anzahl_gewaehlte
- anzahl_gewaehlte_f
- anzahl_gewaehlte_m
- frauen_anteil

## Spalten

- `wahl_jahr`
- `ebene_resultat`
- `geoLevelName`
- `kanton_nummer`
- `kanton_bezeichnung`
- `partei_id`
- `partei_bezeichnung_de`
- `partei_bezeichnung_fr`
- `partei_bezeichnung_it`
- `partei_bezeichnung_en`
- `partei_staerke`
- `flag_staerkste_partei`
- `anzahl_listen`
- `anzahl_kandidierende`
- `anzahl_kandidierende_f`
- `anzahl_kandidierende_m`
- `anzahl_gewaehlte`
- `anzahl_gewaehlte_f`
- `anzahl_gewaehlte_m`
- `frauen_anteil`

## Join Keys

- `local_feature_id`
- `canton_code`
- `sex`
- `vote_or_election_id`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl_gewaehlte | 10 | 44.0, 35.0, 41.0, 25.0, 10.0, 5.0, 3.0, 1.0 |
| anzahl_gewaehlte_f | 10 | 5.0, 4.0, 12.0, 3.0, 1.0, 0.0, 8.0, 19.0 |
| anzahl_gewaehlte_m | 10 | 39.0, 31.0, 29.0, 22.0, 9.0, 4.0, 3.0, 1.0 |
| anzahl_kandidierende | 10 | 267.0, 303.0, 237.0, 35.0, 164.0, 130.0, 11.0, 72.0 |
| anzahl_kandidierende_f | 10 | 72.0, 83.0, 121.0, 40.0, 11.0, 64.0, 38.0, 4.0 |
| anzahl_kandidierende_m | 10 | 195.0, 220.0, 146.0, 197.0, 24.0, 100.0, 92.0, 7.0 |
| anzahl_listen | 10 | 25.0, 36.0, 18.0, 5.0, 10.0, 8.0, 2.0, 6.0 |
| ebene_resultat | 2 | Schweiz, Kanton |
| flag_staerkste_partei | 2 | 1.0, 0.0 |
| frauen_anteil | 10 | 11.363636364, 11.428571429, 29.268292683, 12.0, 10.0, 20.0, 0.0, 100.0 |
| geoLevelName | 10 | Schweiz, Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden |
| kanton_bezeichnung | 10 | Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden, Glarus |
| kanton_nummer | 10 | 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 |
| partei_bezeichnung_de | 10 | FDP, CVP, SP, SVP, LPS, LdU, EVP, CSP |
| partei_bezeichnung_en | 10 | FDP, CVP, SP, SVP, LPS, LdU, EVP, CSP |
| partei_bezeichnung_fr | 10 | PLR, PDC, PS, UDC, PL, AdI, PEV, PCS |
| partei_bezeichnung_it | 10 | PLR, PPD, PS, UDC, PLS, AdI, PEV, PCS |
| partei_id | 10 | 1, 2, 3, 4, 5, 6, 7, 8 |
| partei_staerke | 10 | 20.990763511, 17.999492193, 18.490691992, 11.900966155, 3.0366819685, 2.8285599427, 1.8923146683, 0.3932550395 |
| wahl_jahr | 9 | 1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/nationalratswahlen-zeitreihen-zu-listen-kandidierenden-parteistarken-mandaten-gewahlten-frauen-). Bundesamt für Statistik BFS

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:nationalratswahlen-zeitreihen-zu-listen-kandidierenden-parteistarken-mandaten-gewahlten-frauen-:248576ad-1b14-4dba-b6c9-4ae0f934ea13` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/politics-elections.md) · [Zum Katalog](../Catalog.md)
