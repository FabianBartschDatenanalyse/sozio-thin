# swissdamed: Export der aktiven registrierten Wirtschaftsakteure

| Feld | Wert |
|---|---|
| Thema | [Arbeit und Wirtschaft](../topics/labor-economy.md) |
| Herausgeber | Swissmedic Schweizerisches Heilmittelinstitut |
| Ressourcentyp | ckan_opendata_swiss |
| Format | CSV |
| Zugriff | download_url |
| Zeitraum |  |
| Geografie |  |
| Resource ID | `ckan:bei-der-swissmedic-registrierte-schweizer-und-liechtensteiner-wirtschaftsakteure-medizinprodukt:a9eac020-a65a-4348-a4dd-5e25836617a8` |

## Quelle

[Direkte Datenquelle](https://ogd.swissmedic.cloud/ogd-md/CHRNActors.csv)

## Join Keys

- `local_feature_id`
- `local_area_name`
- `country_code`

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

[Source-specific open-data terms](https://ogd.swissmedic.cloud/ogd-md/CHRNActors.csv). Swissmedic Schweizerisches Heilmittelinstitut

## Verwendung im MCP

1. Mit `get_resource_profile` die Resource ID `ckan:bei-der-swissmedic-registrierte-schweizer-und-liechtensteiner-wirtschaftsakteure-medizinprodukt:a9eac020-a65a-4348-a4dd-5e25836617a8` laden.
2. Den von `search_resources` zurückgegebenen `source_handle` verwenden.
3. Mit `inspect_source` das aktuelle Schema und Beispielwerte prüfen.
4. SQL mit `validate_sql` validieren und danach mit `execute_sql` ausführen.

[Zurück zum Thema](../topics/labor-economy.md) · [Zum Katalog](../Catalog.md)
