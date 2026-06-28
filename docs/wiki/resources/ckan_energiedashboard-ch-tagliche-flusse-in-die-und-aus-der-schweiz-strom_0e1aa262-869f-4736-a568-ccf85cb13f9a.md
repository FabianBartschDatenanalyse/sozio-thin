# energiedashboard.ch: Tägliche Flüsse in die und aus der Schweiz (Strom)-CSV

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | bundesamt-fur-energie-bfe |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:energiedashboard-ch-tagliche-flusse-in-die-und-aus-der-schweiz-strom:0e1aa262-869f-4736-a568-ccf85cb13f9a` |

## Quelle

[Direkte Datenquelle](https://www.bfe-ogd.ch/ogd107_strom_import_export.csv)

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

[Source-specific open-data terms](https://www.bfe-ogd.ch/ogd107_strom_import_export.csv). bundesamt-fur-energie-bfe

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:energiedashboard-ch-tagliche-flusse-in-die-und-aus-der-schweiz-strom:0e1aa262-869f-4736-a568-ccf85cb13f9a` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
