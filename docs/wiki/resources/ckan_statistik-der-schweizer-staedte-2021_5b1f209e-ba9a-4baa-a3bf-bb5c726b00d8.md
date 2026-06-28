# Arbeitslose nach Geschlecht und Sektor, 2019

| Feld | Wert |
|---|---|
| Thema | [Arbeit und Wirtschaft](../topics/labor-economy.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:statistik-der-schweizer-staedte-2021:5b1f209e-ba9a-4baa-a3bf-bb5c726b00d8` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564222/master)

## Join Keys

- `sex`
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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564222/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:statistik-der-schweizer-staedte-2021:5b1f209e-ba9a-4baa-a3bf-bb5c726b00d8` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/labor-economy.md) · [Zum Katalog](../Catalog.md)
