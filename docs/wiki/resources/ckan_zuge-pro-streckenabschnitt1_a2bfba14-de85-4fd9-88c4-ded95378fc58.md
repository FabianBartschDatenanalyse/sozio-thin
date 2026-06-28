# Züge pro Streckenabschnitt

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | Schweizerische Bundesbahnen SBB |
| Ressourcentyp | ckan_opendata_swiss |
| Format | PARQUET |
| Zugriff | download_url |
| Zeitraum | 2021–2025 |
| Geografie |  |
| Resource ID | `ckan:zuge-pro-streckenabschnitt1:a2bfba14-de85-4fd9-88c4-ded95378fc58` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/zuge-pro-streckenabschnitt1) · [Direkte Datenquelle](https://data.sbb.ch/api/v2/catalog/datasets/zugzahlen/exports/parquet)

## Dimensionen

- pid_abschnitt
- isb
- strecke_nummer
- strecke_bezeichnung
- strecke_art
- bp_von_abschnitt
- bp_von_abschnitt_bezeichnung
- bp_bis_abschnitt
- bp_bis_abschnitt_bezeichnung
- in_richtung
- geschaeftscode
- jahr
- anzahl_zuege
- gesamtbelastung_bruttotonnen
- trassenkilometer
- stromverbrauch_auf_abschnitt
- bis_bpuic
- von_bpuic
- verbindung
- geo_point_2d

## Messgrössen

- anzahl_zuege

## Spalten

- `pid_abschnitt`
- `isb`
- `strecke_nummer`
- `strecke_bezeichnung`
- `strecke_art`
- `bp_von_abschnitt`
- `bp_von_abschnitt_bezeichnung`
- `bp_bis_abschnitt`
- `bp_bis_abschnitt_bezeichnung`
- `in_richtung`
- `geschaeftscode`
- `jahr`
- `anzahl_zuege`
- `gesamtbelastung_bruttotonnen`
- `trassenkilometer`
- `stromverbrauch_auf_abschnitt`
- `bis_bpuic`
- `von_bpuic`
- `verbindung`
- `geo_point_2d`

## Join Keys

- `spatial_point`
- `local_feature_id`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| anzahl_zuege | 10 | 2572.0, 222.0, 14607.0, 8730.0, 3279.0, 542.0, 68738.0, 926.0 |
| bis_bpuic | 10 | 8503035, 8503303, 8506041, 8503338, 8518270, 8503149, 8503129, 8503125 |
| bp_bis_abschnitt | 10 | OPS, IL, EMB, HUER, HURW, CHRI, WS, UST |
| bp_bis_abschnitt_bezeichnung | 10 | Opfikon Süd, Illnau, Embrach-Rorbas, Hürlistein (Abzw), Hürlistein West, Chriesbach (Abzw), Wallisellen, Uster |
| bp_von_abschnitt | 10 | ZOEN, EF, BUE, ZSEB, HURW, DTL, WS, ZOER |
| bp_von_abschnitt_bezeichnung | 10 | Zürich Oerlikon Nord (Abzw), Effretikon, Bülach, Zürich Seebach, Hürlistein West, Dietlikon, Wallisellen, Zürich Oerlikon |
| geo_point_2d | 10 | bytearray(b'\x01\x01\x00\x00\x00X$\xae\x05=\x1b!@\xcd\xc7\xe8 \xc8\xb5G@'), bytearray(b'\x01\x01\x00\x00\x00\x86\xa8\x10\xe0\xceh!@\xeeG0\x99j\xb5G@'), bytearray(b'\x01\x01\x00\x00\x00(\xedn&\x8f\x1f!@\xdd\x07\xfc\xbe\xd9\xc2G@'), bytearray(b'\x01\x01\x00\x00\x00\n\x1e\xca{\x1d\x1a!@!Y\xf8\xfb\xf8\xb5G@'), bytearray(b'\x01\x01\x00\x00\x00\xdcjO`\rP!@\xc1\x02]Z3\xb6G@'), bytearray(b'\x01\x01\x00\x00\x00ja\\\xb9\xbfD!@y\x90\xd0\x81\x0e\xb6G@'), bytearray(b'\x01\x01\x00\x00\x00;\xd5\xee1\x964!@\xfb\x02\xd6\xbfI\xb4G@'), bytearray(b'\x01\x01\x00\x00\x00P\x02\x11\\\xd5"!@Ag0\x90\xc0\xb4G@') |
| gesamtbelastung_bruttotonnen | 10 | 990172.0, 201305.0, 1564339.0, 5316788.0, 2253616.0, 186733.0, 25583349.0, 347166.0 |
| geschaeftscode | 2 | Gueterverkehr, Personenverkehr |
| in_richtung | 2 | False, True |
| isb | 9 | SBB, SOB, BLS, HBL, DB, TRAVYS, TPF, HBS |
| jahr | 5 | 2025-01-01 00:00:00, 2024-01-01 00:00:00, 2023-01-01 00:00:00, 2022-01-01 00:00:00, 2021-01-01 00:00:00 |
| pid_abschnitt | 10 | SBB_ZOEN_OPS, SBB_EF_IL, SBB_BUE_EMB, SBB_ZSEB_OPS, SBB_HURW_HUER, SBB_DTL_HURW, SBB_WS_CHRI, SBB_ZOER_WS |
| strecke_art | 2 | STRECKE, KNOTEN |
| strecke_bezeichnung | 10 | Zürich Oerlikon-Nord / Zürich Seebach - Zürich Flughafen / Kloten - Winterthur West, Effretikon - Wetzikon - Hinwil, Winterthur West - Bülach, Zürich Oerlikon - Wallisellen - Hürlistein, Zürich Stadelhofen / Wallisellen - Uster - Rapperswil, Zürich Stadelhofen - Meilen - Rapperswil, Winterthur Grüze - Bauma - Rüti, Winterthur - Neuhausen |
| strecke_nummer | 10 | 62, 66, 68, 63, 64, 65, 67, 69 |
| stromverbrauch_auf_abschnitt | 10 | 25841, 23889, 234482, 164501, 14883, 2896, -81685, 49225 |
| trassenkilometer | 10 | 3014.384000000047, 993.8939999999961, 57551.58000000003, 10860.120000000108, 4079.0760000000864, 674.2480000000038, 74993.15800000096, 2436.305999999996 |
| verbindung | 10 | bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xb5*\xf2\xc7\x1c\x19!@\x95\x9a\xdf\xe37\xb5G@\xfa\x1djC]\x1d!@\x05\xf5\xf1]X\xb6G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\x7fj\xa8h\x94_!@\xd6\xc6s\x02\x81\xb6G@\x8c\xe6xW\tr!@\x07\xc9\xec/T\xb4G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00#9\x1a\x03\x8a\x12!@\x1f\xda\x83\xca\x10\xc3G@.\xa1\xc3I\x94,!@\x9b5t\xb3\xa2\xc2G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\x19\x1e*\xb4\xdd\x16!@=\xbd\xfe\x99\x99\xb5G@\xfa\x1djC]\x1d!@\x05\xf5\xf1]X\xb6G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xdaA\xb7\xa6mL!@\xdb\xd1;\xd5S\xb6G@\xdd\x93\xe7\x19\xadS!@\xa73~\xdf\x12\xb6G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00\xf9\x80\x01\xcc\x11=!@\x17Oe.\xc9\xb5G@\xdaA\xb7\xa6mL!@\xdb\xd1;\xd5S\xb6G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00uR\x866\x11/!@C\xaa.\x1c\xd4\xb4G@\x01XW-\x1b:!@\xb3[}c\xbf\xb3G@'), bytearray(b'\x01\x02\x00\x00\x00\x02\x00\x00\x00,\xb2\x9b\x81\x99\x16!@?$2\x04\xad\xb4G@uR\x866\x11/!@C\xaa.\x1c\xd4\xb4G@') |
| von_bpuic | 10 | 8515494, 8503305, 8503400, 8503007, 8518270, 8503306, 8503129, 8503006 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/zuge-pro-streckenabschnitt1). Schweizerische Bundesbahnen SBB

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:zuge-pro-streckenabschnitt1:a2bfba14-de85-4fd9-88c4-ded95378fc58` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
