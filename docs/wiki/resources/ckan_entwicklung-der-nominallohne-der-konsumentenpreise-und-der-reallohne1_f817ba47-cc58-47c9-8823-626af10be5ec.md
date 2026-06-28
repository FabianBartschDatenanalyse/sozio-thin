# Entwicklung der Nominallöhne, der Konsumentenpreise und der Reallöhne

| Feld | Wert |
|---|---|
| Thema | [Wissenschaft und Forschung](../topics/science-research.md) |
| Herausgeber | bundesamt-fur-statistik-bfs |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:entwicklung-der-nominallohne-der-konsumentenpreise-und-der-reallohne1:f817ba47-cc58-47c9-8823-626af10be5ec` |

## Quelle

[Direkte Datenquelle](https://www.bfs.admin.ch/bfsstatic/dam/assets/17524281/master)

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

[Source-specific open-data terms](https://www.bfs.admin.ch/bfsstatic/dam/assets/17524281/master). bundesamt-fur-statistik-bfs

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:entwicklung-der-nominallohne-der-konsumentenpreise-und-der-reallohne1:f817ba47-cc58-47c9-8823-626af10be5ec` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/science-research.md) · [Zum Katalog](../Catalog.md)
