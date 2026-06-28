# Steuerpflichtige Personen nach Bruttoverm?gens- und Schuldenklasse seit 2020

| Feld | Wert |
|---|---|
| Thema | [Öffentliche Verwaltung und Finanzen](../topics/public-administration-finance.md) |
| Herausgeber | amt-fuer-statistik-fl |
| Ressourcentyp | ckan_opendata_swiss |
| Format | JSON |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:steuerpflichtige-personen-nach-bruttovermogens-und-schuldenklasse-seit-2020:4968be01-2507-4776-95ac-908161da1b57` |

## Quelle

[Direkte Datenquelle](https://etab.llv.li/PXWEb/api/v1/en/eTab//Soziales/Verm?gens-%20und%20Einkommensverteilung/Verm?gen/411.216.px)

## Join Keys

- `year`

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

[Source-specific open-data terms](https://etab.llv.li/PXWEb/api/v1/en/eTab//Soziales/Verm?gens-%20und%20Einkommensverteilung/Verm?gen/411.216.px). amt-fuer-statistik-fl

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:steuerpflichtige-personen-nach-bruttovermogens-und-schuldenklasse-seit-2020:4968be01-2507-4776-95ac-908161da1b57` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/public-administration-finance.md) · [Zum Katalog](../Catalog.md)
