# murs parafeu

| Feld | Wert |
|---|---|
| Thema | [Infrastruktur und Versorgung](../topics/infrastructure-utilities.md) |
| Herausgeber | Schweizerische Bundesbahnen SBB |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 1968–2022 |
| Geografie |  |
| Resource ID | `ckan:brandschutzwand:ef25f25b-2d54-4c82-ac46-66440f8a34a6` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/brandschutzwand) · [Direkte Datenquelle](https://data.sbb.ch/api/v2/catalog/datasets/brandschutzwand/exports/parquet)

## Dimensionen

- n
- e
- linie
- km
- bezeichnung
- lage
- objekt_name
- typ
- be_nr
- material
- bem_material
- b_jahr
- besonderheit
- netz_auf_wand
- h_ab_sok
- lange
- distanz_zu_gl
- fundationsart
- bem_fundation
- eigentumer
- anteil_eigentum
- eigentumer_gruppe
- miteigentumer
- anteil_miteigentum
- miteigentumer_gruppe
- miteigentumer_bemerkung
- lauf_nr
- geopos2
- geopos
- geoshape

## Messgrössen

- anteil_eigentum
- anteil_miteigentum

## Spalten

- `n`
- `e`
- `linie`
- `km`
- `bezeichnung`
- `lage`
- `objekt_name`
- `typ`
- `be_nr`
- `material`
- `bem_material`
- `b_jahr`
- `besonderheit`
- `netz_auf_wand`
- `h_ab_sok`
- `lange`
- `distanz_zu_gl`
- `fundationsart`
- `bem_fundation`
- `eigentumer`
- `anteil_eigentum`
- `eigentumer_gruppe`
- `miteigentumer`
- `anteil_miteigentum`
- `miteigentumer_gruppe`
- `miteigentumer_bemerkung`
- `lauf_nr`
- `geopos2`
- `geopos`
- `geoshape`

## Join Keys

- `spatial_point`
- `local_feature_id`
- `age_group`
- `transport_line_id`
- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anteil_eigentum | 1 | 100 |
| anteil_miteigentum | 0 |  |
| b_jahr | 10 | 1985, 2009, 2020, 2006, 1968, 2010, 2021, 2000 |
| be_nr | 7 | 1, 2, 5, 3, 4, 6, 7 |
| bem_fundation | 10 | muro, Ponte, muro/ponte, Stutzmauer, ringhiera, ponte, posta su muro, posta sopra muro attr. |
| bem_material | 10 | Elements prefabriques, rete, pali con rete, lamiera, Metall, Stahl / HEB 260, 0, solo rete |
| besonderheit | 8 | Oilumschlagplatz, Pallizzata in granito, Verladeschutzwand, Gastank Anlage Quer zur Bahn, alla fine piastra in lamiera, Schutzwand, controventi LNP 120/80/12, Verlade-Schutzwand |
| bezeichnung | 10 | Brand 161.730 BE1, Brand 162.621 BE2, Brand 99.302 BE1, Brand 101.815 BE1, Brand 109.530 BE2, Brand 117.312 BE2, Brand 161.074 BE1, Brand 8.220 BE2 |
| distanz_zu_gl | 10 | 3.03, 3.0, 2.73, 4.14, 3.25, 3.01, 2.31, 2.35 |
| e | 10 | 2715838.567, 2714963.93, 2701206.139, 2701700.103, 2706474.314, 2709277.9, 2716492.796, 2546610.682 |
| eigentumer | 1 | SBB Infrastruktur |
| eigentumer_gruppe | 1 | SBB |
| fundationsart | 4 | Einzelfundament, aufgesetzt auf, Streifenfundament, unbekannt |
| geopos | 10 | bytearray(b'\x01\x01\x00\x00\x00AK\xad\xb93\xe0!@\x08VQ{\x89\x12G@'), bytearray(b"\x01\x01\x00\x00\x00\xce\x9bn\xeae\xda!@\x8f\'\xa41x\x12G@"), bytearray(b'\x01\x01\x00\x00\x00Gf\x83\x0e\x8a\x83!@\xf4mJ\xcc\x1b?G@'), bytearray(b'\x01\x01\x00\x00\x00\x88\xba/\xfa\xc8\x86!@\x96\xa1\xfd\xf4\x9b>G@'), bytearray(b'\x01\x01\x00\x00\x00\x00\xa7\xa0\x97P\xa6!@<\x87Z\xed\x91;G@'), bytearray(b'\x01\x01\x00\x00\x00S\x0eQ\xa4j\xb8!@x$VG\xf65G@'), bytearray(b'\x01\x01\x00\x00\x00\xaa\|\x08\x9b\x8a\xe4!@\x0bQ\x92\xa4\x91\x12G@'), bytearray(b'\x01\x01\x00\x00\x00u\xe4\xf5=\xfa\xf4\x1a@{l\xa4\xaa\xb0fG@') |
| geopos2 | 10 | bytearray(b'\x01\x01\x00\x00\x00\xd5\x88\x9ftx\xde!@\xee\xbe\x93\x8by\x12G@'), bytearray(b"\x01\x01\x00\x00\x00\xc8\x08\xd6\xdd\x9c\xd9!@\x15\xe4\'\xc1v\x12G@"), bytearray(b'\x01\x01\x00\x00\x00\t]\x94V\xb7\x83!@\xdf\xa5\x06\xa3 ?G@'), bytearray(b'\x01\x01\x00\x00\x00\xa8q\xb1\xe1\xd1\x86!@`\xce\xd5\x0c\x9c>G@'), bytearray(b'\x01\x01\x00\x00\x00NY\x89D\x82\xa6!@MA9_};G@'), bytearray(b'\x01\x01\x00\x00\x00\xd2\x0f\xb06\x9d\xb8!@\xe9r\xfe\xfb\xea5G@'), bytearray(b'\x01\x01\x00\x00\x00\x01NhU[\xe2!@O\xf1\x96D\x91\x12G@'), bytearray(b'\x01\x01\x00\x00\x00\xfd\x94\x9e\xa5N\xf5\x1a@A\xbf\xff\x0c\xaffG@') |
| geoshape | 10 | bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xaf@\xad\xb93\xe0!@\x9aJQ{\x89\x12G@\xef\x92\x9ftx\xde!@\xce\xa6\x93\x8by\x12G@'), bytearray(b"\x01\x02\x00\x00\x00\x02\x00\x00\x00\x03\xa1n\xeae\xda!@\xb97\xa41x\x12G@d\x0f\xd6\xdd\x9c\xd9!@\x10\xeb\'\xc1v\x12G@"), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xd9[\x83\x0e\x8a\x83!@\x15\x82J\xcc\x1b?G@t[\x94V\xb7\x83!@p\xa0\x06\xa3 ?G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\x83\xb3/\xfa\xc8\x86!@X\xab\xfd\xf4\x9b>G@\xc5x\xb1\xe1\xd1\x86!@>\xe4\xd5\x0c\x9c>G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xbb\xb0\xa0\x97P\xa6!@W\x8fZ\xed\x91;G@\x03a\x89D\x82\xa6!@\x05<9_};G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00-\x14Q\xa4j\xb8!@")VG\xf65G@\xfd\x08\xb06\x9d\xb8!@\xf5r\xfe\xfb\xea5G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00ku\x08\x9b\x8a\xe4!@\xf9X\x92\xa4\x91\x12G@\xb3HhU[\xe2!@\xf3\xd6\x96D\x91\x12G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x000\xe4\xf5=\xfa\xf4\x1a@;o\xa4\xaa\xb0fG@`\x99\x9e\xa5N\xf5\x1a@\x12\xcd\xff\x0c\xaffG@') |
| h_ab_sok | 10 | 1.9, 2.3, 2.0, 1.8, 1.7, 1.4, 0.0, 1.0 |
| km | 10 | 161.73, 162.621, 99.302, 101.815, 109.53, 117.312, 161.074, 8.22 |
| lage | 3 | rechts der Bahn, links der Bahn, zwischen den Gleisen |
| lange | 10 | 272.56, 118.62, 32.23, 5.23, 80.01, 48.8, 333.56, 10.03 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/brandschutzwand). Schweizerische Bundesbahnen SBB

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:brandschutzwand:ef25f25b-2d54-4c82-ac46-66440f8a34a6` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/infrastructure-utilities.md) · [Zum Katalog](../Catalog.md)
