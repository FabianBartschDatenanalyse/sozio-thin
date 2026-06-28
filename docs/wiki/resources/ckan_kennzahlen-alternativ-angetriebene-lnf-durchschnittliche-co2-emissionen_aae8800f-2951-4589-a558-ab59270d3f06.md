# Durchschnittliche CO2-Emissionen (LNF)

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | bundesamt-fur-energie-bfe |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:kennzahlen-alternativ-angetriebene-lnf-durchschnittliche-co2-emissionen:aae8800f-2951-4589-a558-ab59270d3f06` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/kennzahlen-alternativ-angetriebene-lnf-durchschnittliche-co2-emissionen) · [Direkte Datenquelle](https://www.bfe-ogd.ch/ogd95_data_t4_lnf.csv)

## Dimensionen

- date
- ZH
- BE
- LU
- UR
- SZ
- OW
- NW
- GL
- ZG
- FR
- SO
- BS
- BL
- SH
- AR
- AI
- SG
- GR
- AG
- TG
- TI
- VD
- VS
- NE
- GE
- JU

## Spalten

- `date`
- `ZH`
- `BE`
- `LU`
- `UR`
- `SZ`
- `OW`
- `NW`
- `GL`
- `ZG`
- `FR`
- `SO`
- `BS`
- `BL`
- `SH`
- `AR`
- `AI`
- `SG`
- `GR`
- `AG`
- `TG`
- `TI`
- `VD`
- `VS`
- `NE`
- `GE`
- `JU`

## Join Keys

- `age_group`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| AG | 5 | 178, 226, 211, 196, 203 |
| AI | 5 | 193, 246, 243, 205, 225 |
| AR | 5 | 190, 226, 221, 206, 209 |
| BE | 5 | 177, 219, 202, 192, 195 |
| BL | 5 | 177, 224, 205, 196, 189 |
| BS | 5 | 154, 205, 191, 155, 176 |
| FR | 5 | 172, 211, 206, 197, 191 |
| GE | 5 | 155, 197, 191, 163, 172 |
| GL | 5 | 192, 244, 230, 202, 203 |
| GR | 5 | 192, 238, 223, 205, 211 |
| JU | 5 | 175, 227, 208, 177, 187 |
| LU | 4 | 171, 219, 199, 183 |
| NE | 5 | 166, 218, 192, 198, 187 |
| NW | 5 | 177, 212, 208, 205, 195 |
| OW | 5 | 180, 223, 209, 210, 222 |
| SG | 4 | 179, 221, 189, 191 |
| SH | 5 | 180, 216, 205, 185, 197 |
| SO | 5 | 180, 233, 213, 186, 187 |
| SZ | 4 | 179, 223, 217, 209 |
| TG | 5 | 179, 215, 213, 194, 197 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/kennzahlen-alternativ-angetriebene-lnf-durchschnittliche-co2-emissionen). bundesamt-fur-energie-bfe

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:kennzahlen-alternativ-angetriebene-lnf-durchschnittliche-co2-emissionen:aae8800f-2951-4589-a558-ab59270d3f06` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
