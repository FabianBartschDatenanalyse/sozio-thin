from __future__ import annotations

from pathlib import Path

import duckdb
import httpx

from sozio_thin import pxweb


def test_pxweb_request_retries_temporary_failure(monkeypatch) -> None:
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if calls == 1:
            return httpx.Response(503, request=request)
        return httpx.Response(200, json={"variables": []}, request=request)

    monkeypatch.setattr(pxweb.time, "sleep", lambda _: None)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        response = pxweb._request_with_retry(client, "GET", "https://example.test/table", attempts=2)

    assert response.status_code == 200
    assert calls == 2


def test_csv_to_parquet_writes_readable_output(tmp_path: Path) -> None:
    csv_path = tmp_path / "input.csv"
    parquet_path = tmp_path / "output.parquet"
    csv_path.write_text("Kanton,Wert\nZH,42\n", encoding="utf-8")

    pxweb._convert_csv_to_parquet(csv_path, parquet_path)

    assert parquet_path.exists()
    assert duckdb.connect(":memory:").execute(
        "SELECT Kanton, Wert FROM read_parquet(?)",
        [str(parquet_path)],
    ).fetchall() == [("ZH", 42)]


def test_pxweb_windows_1252_response_is_normalized_to_unicode() -> None:
    request = httpx.Request("POST", "https://example.test/table")
    response = httpx.Response(
        200,
        content='"Kanton","Wert"\r\n"Zürich",42\r\n'.encode("cp1252"),
        headers={"Content-Type": "text/csv; charset=Windows-1252"},
        request=request,
    )

    assert "Zürich" in pxweb._response_text(response)
