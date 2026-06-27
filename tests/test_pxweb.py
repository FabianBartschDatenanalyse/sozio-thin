from __future__ import annotations

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
