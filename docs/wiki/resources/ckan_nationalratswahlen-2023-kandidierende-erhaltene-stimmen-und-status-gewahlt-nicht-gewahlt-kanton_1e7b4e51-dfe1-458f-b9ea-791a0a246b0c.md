# Nationalratswahlen 2023: Kandidierende, erhaltene Stimmen und Status (gewählt/nicht gewählt) (Kantone, Gemeinden)

| Feld | Wert |
|---|---|
| Thema | [Geografie und Raumplanung](../topics/geography-planning.md) |
| Herausgeber | Bundesamt für Statistik BFS |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 1959–2023 |
| Geografie | Canton, Municipality |
| Resource ID | `ckan:nationalratswahlen-2023-kandidierende-erhaltene-stimmen-und-status-gewahlt-nicht-gewahlt-kanton:1e7b4e51-dfe1-458f-b9ea-791a0a246b0c` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/nationalratswahlen-2023-kandidierende-erhaltene-stimmen-und-status-gewahlt-nicht-gewahlt-kanton) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/28845350/appendix)

## Dimensionen

- wahl_jahr
- ebene_resultat
- kanton_nummer
- kanton_bezeichnung
- gemeinde_nummer
- gemeinde_bezeichnung
- liste_nummer_bfs
- liste_nummer_kanton
- liste_bezeichnung
- kandidat_nummer
- name
- vorname
- geschlecht
- geburtsdatum
- geburtsjahr
- wohnort_gemeinde_nummer
- wohnort
- beruf
- kandidat_status_id
- kandidat_status_de
- kandidat_status_fr
- kandidat_status_it
- kandidat_status_en
- kandidat_partei_id
- partei_bezeichnung_de
- partei_bezeichnung_fr
- partei_bezeichnung_it
- partei_bezeichnung_en
- kandidat_listenplatz_1
- kandidat_listenplatz_2
- stimmen_kandidat
- flag_gewaehlt

## Spalten

- `wahl_jahr`
- `ebene_resultat`
- `kanton_nummer`
- `kanton_bezeichnung`
- `gemeinde_nummer`
- `gemeinde_bezeichnung`
- `liste_nummer_bfs`
- `liste_nummer_kanton`
- `liste_bezeichnung`
- `kandidat_nummer`
- `name`
- `vorname`
- `geschlecht`
- `geburtsdatum`
- `geburtsjahr`
- `wohnort_gemeinde_nummer`
- `wohnort`
- `beruf`
- `kandidat_status_id`
- `kandidat_status_de`
- `kandidat_status_fr`
- `kandidat_status_it`
- `kandidat_status_en`
- `kandidat_partei_id`
- `partei_bezeichnung_de`
- `partei_bezeichnung_fr`
- `partei_bezeichnung_it`
- `partei_bezeichnung_en`
- `kandidat_listenplatz_1`
- `kandidat_listenplatz_2`
- `stimmen_kandidat`
- `flag_gewaehlt`

## Join Keys

- `local_feature_id`
- `local_area_name`
- `bfs_municipality_id`
- `canton_code`
- `age_group`
- `sex`
- `occupation`
- `vote_or_election_id`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| beruf | 10 | lic. iur., Unternehmer, Kleinunternehmer, Unternehmer, lic. iur. LL.M., eidg. dipl. Kaminfegermeister, a. Gemeindepräsidentin, eidg. dipl. F/A, eidg. dipl. Landwirt, Präsident Zürcher Bauernverband, Betriebsökonom, Offizier |
| ebene_resultat | 1 | Kanton |
| flag_gewaehlt | 2 | 1, 0 |
| geburtsdatum | 10 | 12.10.1972, 12.10.1961, 23.03.1966, 18.06.1976, 25.01.1972, 11.04.1966, 14.04.1959, 03.05.1962 |
| geburtsjahr | 10 | 1972.0, 1961.0, 1966.0, 1976.0, 1959.0, 1962.0, 1991.0, 1969.0 |
| gemeinde_bezeichnung | 0 |  |
| gemeinde_nummer | 0 |  |
| geschlecht | 2 | M, F |
| kandidat_listenplatz_1 | 10 | 1, 2, 3, 4, 5, 6, 7, 8 |
| kandidat_listenplatz_2 | 10 | 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0 |
| kandidat_nummer | 10 | 1, 2, 3, 4, 5, 6, 7, 8 |
| kandidat_partei_id | 10 | 4, 3, 13, 31, 1, 34, 7, 12 |
| kandidat_status_de | 1 | bisherig |
| kandidat_status_en | 1 | incumbent |
| kandidat_status_fr | 1 | sortant/e |
| kandidat_status_id | 1 | 2.0 |
| kandidat_status_it | 1 | uscente |
| kanton_bezeichnung | 10 | Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden, Glarus |
| kanton_nummer | 10 | 1, 2, 3, 4, 5, 6, 7, 8 |
| liste_bezeichnung | 10 | SVP Schweizerische Volkspartei, SP – Sozialdemokratische Partei, GRÜNE, Grünliberale – GLP, FDP.Die Liberalen, Die Mitte, Evangelische Volkspartei (EVP), AL – Alternative Liste |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/nationalratswahlen-2023-kandidierende-erhaltene-stimmen-und-status-gewahlt-nicht-gewahlt-kanton). Bundesamt für Statistik BFS

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:nationalratswahlen-2023-kandidierende-erhaltene-stimmen-und-status-gewahlt-nicht-gewahlt-kanton:1e7b4e51-dfe1-458f-b9ea-791a0a246b0c` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/geography-planning.md) · [Zum Katalog](../Catalog.md)
