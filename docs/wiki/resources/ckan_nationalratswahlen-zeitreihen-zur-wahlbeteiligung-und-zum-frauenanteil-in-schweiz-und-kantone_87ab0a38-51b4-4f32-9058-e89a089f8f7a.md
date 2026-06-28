# Nationalratswahlen: Zeitreihen zur Wahlbeteiligung und zum Frauenanteil in % (Schweiz und Kantone)

| Feld | Wert |
|---|---|
| Thema | [Politik und Wahlen](../topics/politics-elections.md) |
| Herausgeber | Bundesamt für Statistik BFS |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 1991–2023 |
| Geografie | Canton |
| Resource ID | `ckan:nationalratswahlen-zeitreihen-zur-wahlbeteiligung-und-zum-frauenanteil-in-schweiz-und-kantone:87ab0a38-51b4-4f32-9058-e89a089f8f7a` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/nationalratswahlen-zeitreihen-zur-wahlbeteiligung-und-zum-frauenanteil-in-schweiz-und-kantone) · [Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/28845366/appendix)

## Dimensionen

- wahl_jahr
- ebene_resultat
- geoLevelName
- kanton_nummer
- kanton_bezeichnung
- anzahl_listen
- anzahl_kandidierende
- anzahl_kandidierende_f
- anzahl_kandidierende_m
- anzahl_gewaehlte
- anzahl_gewaehlte_f
- anzahl_gewaehlte_m
- frauen_anteil
- wahlbeteiligung

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
- `anzahl_listen`
- `anzahl_kandidierende`
- `anzahl_kandidierende_f`
- `anzahl_kandidierende_m`
- `anzahl_gewaehlte`
- `anzahl_gewaehlte_f`
- `anzahl_gewaehlte_m`
- `frauen_anteil`
- `wahlbeteiligung`

## Join Keys

- `local_feature_id`
- `canton_code`
- `sex`
- `vote_or_election_id`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl_gewaehlte | 10 | 200, 35, 34, 36, 29, 27, 26, 25 |
| anzahl_gewaehlte_f | 10 | 35, 43, 47, 52, 59, 58, 64, 84 |
| anzahl_gewaehlte_m | 10 | 165, 157, 153, 148, 141, 142, 136, 116 |
| anzahl_kandidierende | 10 | 2561.0, 2834.0, 2845.0, 2836.0, 3089.0, 3458.0, 3788.0, 4645.0 |
| anzahl_kandidierende_f | 10 | 834.0, 990.0, 983.0, 993.0, 1088.0, 1133.0, 1308.0, 1873.0 |
| anzahl_kandidierende_m | 10 | 1727.0, 1844.0, 1862.0, 1843.0, 2001.0, 2325.0, 2480.0, 2772.0 |
| anzahl_listen | 10 | 248.0, 278.0, 268.0, 262.0, 311.0, 365.0, 422.0, 511.0 |
| ebene_resultat | 2 | Schweiz, Kanton |
| frauen_anteil | 10 | 17.5, 21.5, 23.5, 26.0, 29.5, 29.0, 32.0, 42.0 |
| geoLevelName | 10 | Schweiz, Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden |
| kanton_bezeichnung | 10 | Zürich, Bern / Berne, Luzern, Uri, Schwyz, Obwalden, Nidwalden, Glarus |
| kanton_nummer | 10 | 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 |
| wahl_jahr | 9 | 1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019 |
| wahlbeteiligung | 10 | 46.045700707, 42.222231409, 43.303141085, 45.230999305, 48.276098472, 48.504810858, 48.509980778, 45.109775796 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/nationalratswahlen-zeitreihen-zur-wahlbeteiligung-und-zum-frauenanteil-in-schweiz-und-kantone). Bundesamt für Statistik BFS

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:nationalratswahlen-zeitreihen-zur-wahlbeteiligung-und-zum-frauenanteil-in-schweiz-und-kantone:87ab0a38-51b4-4f32-9058-e89a089f8f7a` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/politics-elections.md) · [Zum Katalog](../Catalog.md)
