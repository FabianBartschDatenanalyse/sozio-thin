# Stromnetznutzung vor Wälzung

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | bundesamt-fur-energie-bfe |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2020–2050 |
| Geografie |  |
| Resource ID | `ckan:verteilnetzkosten-strom:e3935617-bc78-4dc6-aaad-5e72fe4c2af7` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/verteilnetzkosten-strom) · [Direkte Datenquelle](https://www.uvek-gis.admin.ch/BFE/ogd/113/ogd113_kosten_netznutzung_vor_waelzung.csv)

## Dimensionen

- ﻿Jahr
- Hauptszenario
- Sensitivitaet
- Modellnetz
- Netzebene
- WACC_prozent
- Kosten_Subtyp
- Kosten_netznutzung_vor_waelzung_chf

## Spalten

- `﻿Jahr`
- `Hauptszenario`
- `Sensitivitaet`
- `Modellnetz`
- `Netzebene`
- `WACC_prozent`
- `Kosten_Subtyp`
- `Kosten_netznutzung_vor_waelzung_chf`

## Join Keys

- `year`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| Hauptszenario | 6 | WWB, ZERO A, ZERO B, ZERO Basis, ZERO C, zusatzSzenarioPV |
| Kosten_Subtyp | 3 | Abschreibungen, Betriebskosten, Kapitalzinsen |
| Kosten_netznutzung_vor_waelzung_chf | 10 | 24503480, 30016763, 16330454, 140843527, 197180937, 112330551, 83859916, 88052912 |
| Modellnetz | 5 | Ganze Schweiz, Grossstädtische Gemeinden, Ländliche Gemeinden, Perirubane Gemeinden, Städtische Gemeinden |
| Netzebene | 6 | NE 2, NE 3, NE 4, NE 5, NE 6, NE 7 |
| Sensitivitaet | 10 | -, Kombination netzorientiertes Verhalten und Spitzenkappung 70%, Kombination netzorientiertes Verhalten und Spitzenkappung 85%, Kombination verstärktes Heimladen und marktorientiertes Verhalten, Kombination verstärktes Heimladen und netzorientiertes Verhalten, Marktorientiertes Ladeverhalten, Netzorientiertes Ladeverhalten, Smarteres Netz |
| WACC_prozent | 1 | 3.83 |
| ﻿Jahr | 7 | 2020, 2025, 2030, 2035, 2040, 2045, 2050 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/verteilnetzkosten-strom). bundesamt-fur-energie-bfe

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:verteilnetzkosten-strom:e3935617-bc78-4dc6-aaad-5e72fe4c2af7` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
