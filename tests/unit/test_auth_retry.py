"""Unit tests for the public refresh methods and the one-shot 401 auto-retry."""

import pytest

from core_client import AsyncClient, Client, CoreAPIError
from core_client.base.models import Error


# --- one-shot 401 retry (sync) -------------------------------------------------


def _make_sync_client(responses):
    """A Client whose proxy calls a fake api function returning `responses` in order."""
    calls = {"n": 0}

    def fake_sync(client, **kwargs):
        i = calls["n"]
        calls["n"] += 1
        return responses[i]

    client = Client(base_url="http://x", access_token="dummy")
    client._probe = Client._make_proxy_method(fake_sync).__get__(client, Client)
    return client, calls


def test_sync_401_then_200_retries_once():
    client, calls = _make_sync_client([Error(code=401, message="u", details=[]), "OK"])
    assert client._probe() == "OK"
    assert calls["n"] == 2


def test_sync_401_then_401_returns_error():
    client, calls = _make_sync_client(
        [Error(code=401, message="u", details=[]), Error(code=401, message="u", details=[])]
    )
    result = client._probe()
    assert isinstance(result, Error) and result.code == 401
    assert calls["n"] == 2


def test_sync_401_then_401_raises_with_raise_on_error():
    client, calls = _make_sync_client(
        [Error(code=401, message="u", details=[]), Error(code=401, message="u", details=[])]
    )
    client.raise_on_error = True
    with pytest.raises(CoreAPIError) as exc:
        client._probe()
    assert exc.value.code == 401
    assert calls["n"] == 2


def test_sync_non_401_error_is_not_retried():
    client, calls = _make_sync_client([Error(code=404, message="nf", details=[])])
    result = client._probe()
    assert isinstance(result, Error) and result.code == 404
    assert calls["n"] == 1


# --- one-shot 401 retry (async) ------------------------------------------------


def _make_async_client(responses):
    calls = {"n": 0}

    async def fake_asyncio(client, **kwargs):
        i = calls["n"]
        calls["n"] += 1
        return responses[i]

    client = AsyncClient(base_url="http://x", access_token="dummy")
    client._probe = AsyncClient._make_proxy_method(fake_asyncio).__get__(client, AsyncClient)
    return client, calls


async def test_async_401_then_200_retries_once():
    client, calls = _make_async_client([Error(code=401, message="u", details=[]), "OK"])
    assert await client._probe() == "OK"
    assert calls["n"] == 2


async def test_async_401_then_401_returns_error():
    client, calls = _make_async_client(
        [Error(code=401, message="u", details=[]), Error(code=401, message="u", details=[])]
    )
    result = await client._probe()
    assert isinstance(result, Error) and result.code == 401
    assert calls["n"] == 2


# --- public refresh ------------------------------------------------------------


def test_refresh_calls_refresh_under_lock(monkeypatch):
    client = Client(base_url="http://x", access_token="a", refresh_token="r")
    seen = {"n": 0}
    monkeypatch.setattr(client, "_refresh_access_token", lambda: seen.__setitem__("n", seen["n"] + 1))
    tok = client.refresh()
    assert seen["n"] == 1
    assert tok.access_token == "a"


async def test_arefresh_calls_refresh_under_lock(monkeypatch):
    client = AsyncClient(base_url="http://x", access_token="a", refresh_token="r")
    seen = {"n": 0}

    async def fake():
        seen["n"] += 1

    monkeypatch.setattr(client, "_arefresh_access_token", fake)
    tok = await client.arefresh()
    assert seen["n"] == 1
    assert tok.access_token == "a"
