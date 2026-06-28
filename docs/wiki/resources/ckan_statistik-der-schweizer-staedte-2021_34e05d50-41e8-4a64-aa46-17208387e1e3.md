# Steuerbelastung in der Schweiz: Natürliche Personen - Lediger, ein Einkommen, ohne Kinder, 2019

| Feld | Wert |
|---|---|
| Thema | [Öffentliche Verwaltung und Finanzen](../topics/public-administration-finance.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:statistik-der-schweizer-staedte-2021:34e05d50-41e8-4a64-aa46-17208387e1e3` |

## Quelle

[Direkte Datenquelle](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564368/master)

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

[Source-specific open-data terms](https://dam-api.bfs.admin.ch/hub/api/dam/assets/16564368/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:statistik-der-schweizer-staedte-2021:34e05d50-41e8-4a64-aa46-17208387e1e3` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/public-administration-finance.md) · [Zum Katalog](../Catalog.md)
