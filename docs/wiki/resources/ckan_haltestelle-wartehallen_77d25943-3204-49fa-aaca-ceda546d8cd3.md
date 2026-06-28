# Stop: waiting rooms

| Feld | Wert |
|---|---|
| Thema | [Wohnen und Bau](../topics/housing-construction.md) |
| Herausgeber | Schweizerische Bundesbahnen SBB |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie | Canton, Municipality |
| Resource ID | `ckan:haltestelle-wartehallen:77d25943-3204-49fa-aaca-ceda546d8cd3` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/haltestelle-wartehallen) · [Direkte Datenquelle](https://data.sbb.ch/api/v2/catalog/datasets/haltestelle-wartehallen/exports/parquet)

## Dimensionen

- linie
- km
- gebaudename
- strasse
- anzahl_untergeschosse
- anzahl_obergeschosse
- gebaudetyp
- plz
- ort
- gemeinde
- kanton
- status
- geopos
- bpuic
- bezeichnung_offiziell
- abkuerzung
- lod
- tu_nummer
- dst_id
- sloid

## Messgrössen

- anzahl_untergeschosse
- anzahl_obergeschosse

## Spalten

- `linie`
- `km`
- `gebaudename`
- `strasse`
- `anzahl_untergeschosse`
- `anzahl_obergeschosse`
- `gebaudetyp`
- `plz`
- `ort`
- `gemeinde`
- `kanton`
- `status`
- `geopos`
- `bpuic`
- `bezeichnung_offiziell`
- `abkuerzung`
- `lod`
- `tu_nummer`
- `dst_id`
- `sloid`

## Join Keys

- `spatial_point`
- `local_feature_id`
- `bfs_municipality_id`
- `canton_code`
- `age_group`
- `building_or_dwelling`
- `transport_stop_id`
- `transport_line_id`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| abkuerzung | 10 | AA, ABO, ALN, AS, AVRY, BDR, BEL, BET |
| anzahl_obergeschosse | 2 | 1, 0 |
| anzahl_untergeschosse | 2 | 0, 1 |
| bezeichnung_offiziell | 10 | Aarau, Aarburg-Oftringen, Altnau, Amsteg-Silenen, Avry-Matran, Boudry, Bellinzona, Bettlach |
| bpuic | 10 | 8502113, 8502000, 8506125, 8505115, 8501632, 8504208, 8505213, 8500203 |
| dst_id | 10 | 2113, 2000, 6125, 5115, 1632, 4208, 5213, 203 |
| gebaudename | 10 | Wartehalle, Wartehalle offen Gleis 2, Haltestelle Intschi (mit Technik), Quai 2, RV 05, sala d'aspetta chiusa, Abri voyageurs, Offene Wartehalle Typ RV05 / Seetal |
| gebaudetyp | 9 | Wartehalle 94, Wartehalle 75, Andere (SBB / ZB), Wartehalle 04, Wartehalle 08, Wartehalle 81, kein Normtyp, Unterstand 94 |
| gemeinde | 10 | Aarau, Aarburg, Altnau, Silenen, Avry, Boudry, Bellinzona, Bettlach |
| geopos | 10 | bytearray(b'\x01\x01\x00\x00\x00x\xed\x81\x8c@\x1a @7+\x8d\x11\x18\xb2G@'), bytearray(b'\x01\x01\x00\x00\x00\xb2ce\x1b\x05\xa2\x1f@\xeb5\xa5\x8e\xfe\xa8G@'), bytearray(b'\x01\x01\x00\x00\x00D\xd5\x0ef&\x88"@\xd5\x03\x02\xfc\x88\xcfG@'), bytearray(b'\x01\x01\x00\x00\x00\xc8m\xc97\x1eX!@\x88\xfd\xa9\xdf\xf7cG@'), bytearray(b'\x01\x01\x00\x00\x00\xed\x84\xd1o]R\x1c@\xdcm\xf9\xa2\x9cdG@'), bytearray(b'\x01\x01\x00\x00\x00\x06\x91n\xb9\x16W\x1b@\xd1\xc7e}\xcfzG@'), bytearray(b'\x01\x01\x00\x00\x00s\xad\xe9\x0c\x1d\x0f"@\xa9\x0f\xb2\xe8\x03\x19G@'), bytearray(b'\x01\x01\x00\x00\x00&\xc7\x85j\xa7\xb6\x1d@`B8\x1a\xf4\x98G@') |
| kanton | 10 | AG, TG, UR, FR, NE, TI, SO, BE |
| km | 10 | 41.34312, 42.918227, 92.848411, 49.954794, 58.998794, 66.247156, 150.825286, 82.937419 |
| linie | 10 | 650, 500, 824, 600, 250, 210, 410, 260 |
| lod | 1 | http://lod.opentransportdata.swiss/didok/didok85 |
| ort | 10 | Aarau, Aarburg, Altnau, Amsteg, Avry-sur-Matran, Boudry, Bellinzona, Bettlach |
| plz | 10 | 5000, 4663, 8595, 6474, 1754, 2017, 6500, 2544 |
| sloid | 10 | ch:1:sloid:2113, ch:1:sloid:2000, ch:1:sloid:6125, ch:1:sloid:5115, ch:1:sloid:1632, ch:1:sloid:4208, ch:1:sloid:5213, ch:1:sloid:203 |
| status | 3 | BESTEHEND, PROJEKTIERT NEU, PROJEKTIERT ABBRUCH |
| strasse | 10 | Hintere Bahnhofstrasse, Bahnhofstrasse Perron 2, Bahnhofstrasse, Spitzacher, km 49.95, Quai 2, Marciapiede 2 Nord, Perron 2, Perron 2/3 |
| tu_nummer | 1 | 11 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/haltestelle-wartehallen). Schweizerische Bundesbahnen SBB

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:haltestelle-wartehallen:77d25943-3204-49fa-aaca-ceda546d8cd3` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/housing-construction.md) · [Zum Katalog](../Catalog.md)
