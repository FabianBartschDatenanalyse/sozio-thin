# Schweizerischer Lohnindex: Index und Veränderung auf der Basis 2020 = 100 (NOGA08)

| Feld | Wert |
|---|---|
| Thema | [Arbeit und Wirtschaft](../topics/labor-economy.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:schweizerischer-lohnindex-index-und-veranderung-auf-der-basis-2020-100-noga08:5c1f111b-1237-4ec0-aa21-88bd3113fb61` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36506631/master)

## Join Keys

- `sex`
- `economic_activity`
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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36506631/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:schweizerischer-lohnindex-index-und-veranderung-auf-der-basis-2020-100-noga08:5c1f111b-1237-4ec0-aa21-88bd3113fb61` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/labor-economy.md) · [Zum Katalog](../Catalog.md)
