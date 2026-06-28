# DATA - Energieforschungsstatistik (EFstat) gemäss Klassifikation der Internationalen Energieagentur

| Feld | Wert |
|---|---|
| Thema | [Umwelt, Energie und Klima](../topics/environment-energy-climate.md) |
| Herausgeber | bundesamt-fur-energie-bfe |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:energieforschungsstatistik-efstat:fe86ad62-1455-4658-8f81-c13e626dbd27` |

## Quelle

[Direkte Datenquelle](https://www.uvek-gis.admin.ch/BFE/ogd/10/ogd10_energieforschungstatistik_iea.csv)

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

[Source-specific open-data terms](https://www.uvek-gis.admin.ch/BFE/ogd/10/ogd10_energieforschungstatistik_iea.csv). bundesamt-fur-energie-bfe

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:energieforschungsstatistik-efstat:fe86ad62-1455-4658-8f81-c13e626dbd27` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/environment-energy-climate.md) · [Zum Katalog](../Catalog.md)
