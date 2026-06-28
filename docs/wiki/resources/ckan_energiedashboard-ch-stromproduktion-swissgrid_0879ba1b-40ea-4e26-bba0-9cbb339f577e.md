# energiedashboard.ch: Stromproduktion Swissgrid-CSV

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | bundesamt-fur-energie-bfe |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:energiedashboard-ch-stromproduktion-swissgrid:0879ba1b-40ea-4e26-bba0-9cbb339f577e` |

## Quelle

[Direkte Datenquelle](https://www.bfe-ogd.ch/ogd104_stromproduktion_swissgrid.csv)

## Join Keys

- `date`

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

[Source-specific open-data terms](https://www.bfe-ogd.ch/ogd104_stromproduktion_swissgrid.csv). bundesamt-fur-energie-bfe

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:energiedashboard-ch-stromproduktion-swissgrid:0879ba1b-40ea-4e26-bba0-9cbb339f577e` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
