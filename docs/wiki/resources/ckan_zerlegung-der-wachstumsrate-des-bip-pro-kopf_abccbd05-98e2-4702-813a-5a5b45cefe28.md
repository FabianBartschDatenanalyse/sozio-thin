# Zerlegung der Wachstumsrate des BIP pro Kopf

| Feld | Wert |
|---|---|
| Thema | [Arbeit und Wirtschaft](../topics/labor-economy.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:zerlegung-der-wachstumsrate-des-bip-pro-kopf:abccbd05-98e2-4702-813a-5a5b45cefe28` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36191843/master)

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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36191843/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:zerlegung-der-wachstumsrate-des-bip-pro-kopf:abccbd05-98e2-4702-813a-5a5b45cefe28` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/labor-economy.md) · [Zum Katalog](../Catalog.md)
