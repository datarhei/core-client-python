"""Unit tests for the robustness features from CLIENT-TODO §2."""

import httpx
import pytest

from core_client import AsyncClient, Client, CoreAPIError
from core_client.base.models import Error


def _error():
    return Error(code=404, message="Not Found", details=["Not Found"])


# --- §2.6 raise_on_error --------------------------------------------------


def test_raise_on_error_raises_for_error_result():
    client = Client(base_url="http://example.com", raise_on_error=True)
    with pytest.raises(CoreAPIError) as exc_info:
        client._raise_if_error(_error())
    assert exc_info.value.code == 404
    assert exc_info.value.message == "Not Found"


def test_raise_on_error_passes_through_non_error():
    client = Client(base_url="http://example.com", raise_on_error=True)
    assert client._raise_if_error("ok") == "ok"


def test_default_returns_error_without_raising():
    client = Client(base_url="http://example.com")
    result = client._raise_if_error(_error())
    assert isinstance(result, Error)


def test_core_api_error_carries_error_model():
    err = _error()
    exc = CoreAPIError(err)
    assert exc.error is err
    assert exc.code == 404 and exc.message == "Not Found"
    assert isinstance(exc, httpx.HTTPError)


# --- §2.3 connection pooling / lifecycle ----------------------------------


def test_sync_pooled_client_is_reused():
    client = Client(base_url="http://example.com")
    assert client._http_client is None
    first = client._pooled_http_client()
    assert first is client._pooled_http_client()
    assert isinstance(first, httpx.Client)
    client.close()
    assert client._http_client is None


def test_sync_client_context_manager_closes_pool():
    with Client(base_url="http://example.com") as client:
        client._pooled_http_client()
        assert client._http_client is not None
    assert client._http_client is None


async def test_async_pooled_client_is_reused_and_closes():
    client = AsyncClient(base_url="http://example.com")
    first = client._pooled_async_http_client()
    assert first is client._pooled_async_http_client()
    assert isinstance(first, httpx.AsyncClient)
    await client.aclose()
    assert getattr(client, "_async_http_client", None) is None


async def test_async_client_context_manager_closes_pool():
    async with AsyncClient(base_url="http://example.com") as client:
        client._pooled_async_http_client()
        assert client._async_http_client is not None
    assert getattr(client, "_async_http_client", None) is None
