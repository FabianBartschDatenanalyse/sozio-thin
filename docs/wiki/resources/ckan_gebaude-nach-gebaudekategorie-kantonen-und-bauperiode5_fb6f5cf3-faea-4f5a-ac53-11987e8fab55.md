# Gebäude nach Gebäudekategorie, Kantonen und Bauperiode

| Feld | Wert |
|---|---|
| Thema | [Wohnen und Bau](../topics/housing-construction.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie | Canton |
| Resource ID | `ckan:gebaude-nach-gebaudekategorie-kantonen-und-bauperiode5:fb6f5cf3-faea-4f5a-ac53-11987e8fab55` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36158426/master)

## Join Keys

- `canton_code`
- `building_or_dwelling`
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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36158426/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:gebaude-nach-gebaudekategorie-kantonen-und-bauperiode5:fb6f5cf3-faea-4f5a-ac53-11987e8fab55` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/housing-construction.md) · [Zum Katalog](../Catalog.md)
