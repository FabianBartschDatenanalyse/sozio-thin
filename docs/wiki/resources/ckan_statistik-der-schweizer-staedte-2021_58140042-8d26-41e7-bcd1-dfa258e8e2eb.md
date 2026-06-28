# Kommunale Einnahmen - Bereich Kultur, Sport und Freizeit, 2018

| Feld | Wert |
|---|---|
| Thema | [Kultur, Sport und Tourismus](../topics/culture-sport-tourism.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:statistik-der-schweizer-staedte-2021:58140042-8d26-41e7-bcd1-dfa258e8e2eb` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564342/master)

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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564342/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:statistik-der-schweizer-staedte-2021:58140042-8d26-41e7-bcd1-dfa258e8e2eb` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/culture-sport-tourism.md) · [Zum Katalog](../Catalog.md)
