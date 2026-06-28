# Beschuldigte nach Straftat, einzelne Delikte

| Feld | Wert |
|---|---|
| Thema | [Justiz, Polizei und Sicherheit](../topics/justice-police-safety.md) |
| Herausgeber | kanton-zug |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2009–2018 |
| Geografie |  |
| Resource ID | `ckan:beschuldigte-gemass-strafgesetzbuch-nach-straftat:9ebb6bd7-fe55-4b71-b0fb-41256defcbb5` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/beschuldigte-gemass-strafgesetzbuch-nach-straftat) · [Direkte Datenquelle](https://data.zg.ch/store/1/resource/1399)

## Dimensionen

- jahr
- kategorie
- straftat
- anzahl

## Messgrössen

- anzahl

## Spalten

- `jahr`
- `kategorie`
- `straftat`
- `anzahl`

## Join Keys

- `offence_type`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl | 10 | 221, 178, 174, 158, 140, 100, 79, 76 |
| jahr | 10 | 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016 |
| kategorie | 10 | Leib und Leben, Vermögen, Freiheit, Ehre-, Geheim-, Privatbereich, Öffentliche Gewalt, Urkundenfälschung, Bundesrechtliche Bestimmungen, Sexuelle Integrität |
| straftat | 10 | Tätlichkeiten (Art. 126), Sachbeschädigung (Art. 144), Ladendiebstahl (Art. 139), Drohung (Art. 180), Einfache Körperverletzung (Art. 123), Hausfriedensbruch und Diebstahl (Art. 186), Sachbeschädigung und Diebstahl (Art. 144), Einbruchdiebstahl (Art. 139) |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/beschuldigte-gemass-strafgesetzbuch-nach-straftat). kanton-zug

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:beschuldigte-gemass-strafgesetzbuch-nach-straftat:9ebb6bd7-fe55-4b71-b0fb-41256defcbb5` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/justice-police-safety.md) · [Zum Katalog](../Catalog.md)
