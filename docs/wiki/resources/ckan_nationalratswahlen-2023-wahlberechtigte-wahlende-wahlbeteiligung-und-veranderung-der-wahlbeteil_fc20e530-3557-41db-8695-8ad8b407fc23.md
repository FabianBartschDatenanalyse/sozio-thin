# Nationalratswahlen 2023: Wahlberechtigte, Wählende, Wahlbeteiligung und Veränderung der Wahlbeteiligung (Schweiz, Kantone, Gemeinden)

| Feld | Wert |
|---|---|
| Thema | [Politik und Wahlen](../topics/politics-elections.md) |
| Herausgeber | Bundesamt für Statistik BFS |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2023 |
| Geografie | Canton, Municipality |
| Resource ID | `ckan:nationalratswahlen-2023-wahlberechtigte-wahlende-wahlbeteiligung-und-veranderung-der-wahlbeteil:fc20e530-3557-41db-8695-8ad8b407fc23` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/nationalratswahlen-2023-wahlberechtigte-wahlende-wahlbeteiligung-und-veranderung-der-wahlbeteil) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/28845368/appendix)

## Dimensionen

- wahl_jahr
- ebene_resultat
- geoLevelName
- kanton_nummer
- kanton_bezeichnung
- bezirk_nummer
- bezirk_bezeichnung
- gemeinde_nummer
- gemeinde_bezeichnung
- wahlberechtigte
- leere_wahlzettel
- ungueltige_wahlzettel
- gueltige_wahlzettel
- wahlbeteiligung
- letzte_wahl_wahlbeteiligung
- differenz_wahlbeteiligung
- eingelegte_wahlzettel

## Spalten

- `wahl_jahr`
- `ebene_resultat`
- `geoLevelName`
- `kanton_nummer`
- `kanton_bezeichnung`
- `bezirk_nummer`
- `bezirk_bezeichnung`
- `gemeinde_nummer`
- `gemeinde_bezeichnung`
- `wahlberechtigte`
- `leere_wahlzettel`
- `ungueltige_wahlzettel`
- `gueltige_wahlzettel`
- `wahlbeteiligung`
- `letzte_wahl_wahlbeteiligung`
- `differenz_wahlbeteiligung`
- `eingelegte_wahlzettel`

## Join Keys

- `local_feature_id`
- `bfs_municipality_id`
- `canton_code`
- `vote_or_election_id`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| bezirk_bezeichnung | 10 | Bezirk Affoltern, Bezirk Andelfingen, Bezirk Bülach, Bezirk Dielsdorf, Bezirk Hinwil, Bezirk Horgen, Bezirk Meilen, Bezirk Pfäffikon |
| bezirk_nummer | 10 | 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0 |
| differenz_wahlbeteiligung | 10 | 1.5475927734, 2.5127391591, 2.3724957588, 1.8654394315, 4.6286183089, 5.9638576568, 3.6726558159, 5.8208348577 |
| ebene_resultat | 3 | Schweiz, Kanton, Gemeinde |
| eingelegte_wahlzettel | 10 | 2604984, 454092, 371818, 143512, 13667, 58790, 16201, 17953 |
| gemeinde_bezeichnung | 10 | Aeugst am Albis, Affoltern am Albis, Bonstetten, Hausen am Albis, Hedingen, Kappel am Albis, Knonau, Maschwanden |
| gemeinde_nummer | 10 | 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 |
| geoLevelName | 10 | Schweiz, Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden |
| gueltige_wahlzettel | 10 | 2554482, 447232, 367180, 139906, 13282, 58225, 15711, 17701 |
| kanton_bezeichnung | 10 | Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden, Glarus |
| kanton_nummer | 10 | 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 |
| leere_wahlzettel | 10 | 9523, 188, 430, 239, 286, 59, 265, 165 |
| letzte_wahl_wahlbeteiligung | 10 | 45.109775796, 44.439305012, 47.376696425, 48.387027461, 45.860871513, 48.647804102, 55.077706818, 50.384161699 |
| ungueltige_wahlzettel | 10 | 40979, 6672, 4208, 3367, 99, 506, 225, 87 |
| wahl_jahr | 1 | 2023 |
| wahlberechtigte | 10 | 5583221, 967140, 747385, 285582, 27069, 107651, 27576, 31942 |
| wahlbeteiligung | 10 | 46.657368569, 46.952044171, 49.749192183, 50.252466892, 50.489489822, 54.611661759, 58.750362634, 56.204996556 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/nationalratswahlen-2023-wahlberechtigte-wahlende-wahlbeteiligung-und-veranderung-der-wahlbeteil). Bundesamt für Statistik BFS

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:nationalratswahlen-2023-wahlberechtigte-wahlende-wahlbeteiligung-und-veranderung-der-wahlbeteil:fc20e530-3557-41db-8695-8ad8b407fc23` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/politics-elections.md) · [Zum Katalog](../Catalog.md)
