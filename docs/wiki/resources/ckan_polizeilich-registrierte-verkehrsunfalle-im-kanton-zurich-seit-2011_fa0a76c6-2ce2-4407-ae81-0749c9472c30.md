# Polizeilich registrierte Verkehrsunfälle im Kanton Zürich

| Feld | Wert |
|---|---|
| Thema | [Mobilität und Verkehr](../topics/mobility-transport.md) |
| Herausgeber | Kantonspolizei Zürich |
| Ressourcentyp | ckan_opendata_swiss |
| Format | JSON |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie | Canton |
| Resource ID | `ckan:polizeilich-registrierte-verkehrsunfalle-im-kanton-zurich-seit-2011:fa0a76c6-2ce2-4407-ae81-0749c9472c30` |

## Quelle

[Direkte Datenquelle](https://daten.statistik.zh.ch/ogd/daten/ressourcen/KTZH_00000718_00001795.json)

## Join Keys

- `canton_code`
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

[Source-specific open-data terms](https://daten.statistik.zh.ch/ogd/daten/ressourcen/KTZH_00000718_00001795.json). Kantonspolizei Zürich

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:polizeilich-registrierte-verkehrsunfalle-im-kanton-zurich-seit-2011:fa0a76c6-2ce2-4407-ae81-0749c9472c30` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/mobility-transport.md) · [Zum Katalog](../Catalog.md)
