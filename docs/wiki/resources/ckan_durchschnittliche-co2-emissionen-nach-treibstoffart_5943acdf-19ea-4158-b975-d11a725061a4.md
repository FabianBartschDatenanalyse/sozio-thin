# Durchschnittliche CO2-Emissionen nach Treibstoffart (PW)

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | Bundesamt für Energie BFE |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum | 2015–2024 |
| Geografie | Canton |
| Resource ID | `ckan:durchschnittliche-co2-emissionen-nach-treibstoffart:5943acdf-19ea-4158-b975-d11a725061a4` |

## Quelle

[Datensatzseite](https://opendata.swiss/de/dataset/durchschnittliche-co2-emissionen-nach-treibstoffart) · [Direkte Datenquelle](https://www.bfe-ogd.ch/ogd92_data-ch.csv)

## Dimensionen

- Kanton
- Year
- Quarter
- Month
- t13
- t14
- t15
- t16
- t17
- t18
- t19
- t20
- t21

## Spalten

- `Kanton`
- `Year`
- `Quarter`
- `Month`
- `t13`
- `t14`
- `t15`
- `t16`
- `t17`
- `t18`
- `t19`
- `t20`
- `t21`

## Join Keys

- `canton_code`
- `year`
- `date`

## Beispielwerte

| Feld | Anzahl | Beispiele |
|---|---:|---|
| Kanton | 2 | 28, 31 |
| Month | 10 | 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 |
| Quarter | 5 | 1.0, 2.0, 3.0, 4.0, 5.0 |
| Year | 10 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 |
| t13 | 1 | 0 |
| t14 | 10 | 43, 33, 40, 39, 38, 51, 47, 52 |
| t15 | 10 | 45.0, 47.0, 48.0, 49.0, 44.0, 37.0, 40.0, 39.0 |
| t16 | 10 | 97, 93, 91, 95, 96, 101, 98, 104 |
| t17 | 10 | 103, 105, 100, 102, 101, 104, 113, 107 |
| t18 | 10 | 96.0, 95.0, 98.0, 94.0, 93.0, 92.0, 99.0, 102.0 |
| t19 | 1 | 0.0 |
| t20 | 10 | 138, 136, 135, 137, 139, 142, 144, 145 |
| t21 | 10 | 143, 141, 139, 137, 140, 136, 138, 142 |

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

[Source-specific open-data terms](https://opendata.swiss/de/dataset/durchschnittliche-co2-emissionen-nach-treibstoffart). Bundesamt für Energie BFE

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:durchschnittliche-co2-emissionen-nach-treibstoffart:5943acdf-19ea-4158-b975-d11a725061a4` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
