"""Shared HTTP execution helpers for the generated API modules.

Centralizes request execution so every endpoint benefits from:

* connection pooling — a persistent ``httpx`` client per ``Client`` instance is
  reused across calls instead of opening a fresh connection per request
  (CLIENT-TODO §2.3);
* consistent HTTP/2 — both the sync and async paths enable it (§2.4).

A pooled client is used when the caller did not override ``retries`` (retries
are a transport-level setting, so a per-request override falls back to a
short-lived client). When no pooled client is attached, a per-request client is
created, preserving the previous behavior.
"""

import httpx


def execute_sync(client, request, retries):
    pooled = getattr(client, "http_client", None)
    if pooled is not None and retries == client.retries:
        return pooled.request(**request)
    transport = httpx.HTTPTransport(retries=retries)
    with httpx.Client(transport=transport, http2=True) as httpx_client:
        return httpx_client.request(**request)


async def execute_async(client, request, retries):
    pooled = getattr(client, "http_client", None)
    if pooled is not None and retries == client.retries:
        return await pooled.request(**request)
    transport = httpx.AsyncHTTPTransport(retries=retries)
    async with httpx.AsyncClient(transport=transport, http2=True) as httpx_client:
        return await httpx_client.request(**request)
