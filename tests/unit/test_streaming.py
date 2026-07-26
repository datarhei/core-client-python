"""Unit tests for the async event-streaming core (`_stream.stream_events`)."""

import asyncio
import time
import types

import httpx
import pytest

from core_client.base.api import _stream
from core_client.exceptions import CoreAPIError


class _MockStream(httpx.AsyncByteStream):
    """Async byte stream that yields the given chunks, optionally endlessly."""

    def __init__(self, chunks, *, endless_after=None, delay=0.0):
        self._chunks = chunks
        self._endless_after = endless_after
        self._delay = delay
        self.closed = False

    async def __aiter__(self):
        for chunk in self._chunks:
            if self._delay:
                await asyncio.sleep(self._delay)
            yield chunk
        if self._endless_after is not None:
            # Simulate an endless stream that never sends EOF.
            while True:
                await asyncio.sleep(0.01)
                yield self._endless_after

    async def aclose(self):
        self.closed = True


def _client(status=200, content_type="text/event-stream", stream=None, body=b""):
    def handler(request):
        if stream is not None:
            return httpx.Response(status, headers={"content-type": content_type}, stream=stream)
        return httpx.Response(status, headers={"content-type": content_type}, content=body)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler), http2=False)


def _patch(monkeypatch, client):
    monkeypatch.setattr(_stream, "_make_stream_client", lambda: client)


def _stub_client_model():
    return types.SimpleNamespace(headers={}, timeout=5.0)


async def _collect(agen, limit):
    out = []
    async for item in agen:
        out.append(item)
        if len(out) >= limit:
            break
    return out


# --- frame mode (SSE + NDJSON) -------------------------------------------------


async def test_frame_mode_parses_sse(monkeypatch):
    lines = [
        b":keepalive\n",
        b"event: ProcessReport\n",
        b'data: {"a": 1}\n',
        b"\n",
        b'data: {"b": 2}\n',  # after blank line -> event_type resets to "message"
    ]
    _patch(monkeypatch, _client(stream=_MockStream(lines)))
    got = await _collect(_stream.stream_events(_stub_client_model(), "POST", "http://x"), 2)
    assert got == [("ProcessReport", '{"a": 1}'), ("message", '{"b": 2}')]


async def test_frame_mode_delivers_raw_ndjson(monkeypatch):
    lines = [b'{"pid": "p1", "type": "progress"}\n', b'{"pid": "p2", "type": "progress"}\n']
    _patch(monkeypatch, _client(content_type="application/x-json-stream", stream=_MockStream(lines)))
    got = await _collect(_stream.stream_events(_stub_client_model(), "POST", "http://x"), 2)
    assert got == [
        ("message", '{"pid": "p1", "type": "progress"}'),
        ("message", '{"pid": "p2", "type": "progress"}'),
    ]


async def test_raw_mode_yields_lines(monkeypatch):
    lines = [b":keepalive\n", b'data: {"a": 1}\n']
    _patch(monkeypatch, _client(stream=_MockStream(lines)))
    got = await _collect(_stream.stream_events(_stub_client_model(), "POST", "http://x", frame=False), 2)
    assert got == [":keepalive", 'data: {"a": 1}']


# --- lifecycle -----------------------------------------------------------------


async def test_eof_ends_generator(monkeypatch):
    _patch(monkeypatch, _client(stream=_MockStream([b'data: {"a": 1}\n'])))
    got = [item async for item in _stream.stream_events(_stub_client_model(), "POST", "http://x")]
    assert got == [("message", '{"a": 1}')]


async def test_endless_stream_is_event_wise_and_closes(monkeypatch):
    stream = _MockStream([b'data: {"n": 0}\n'], endless_after=b'data: {"n": 1}\n')
    _patch(monkeypatch, _client(stream=stream))
    agen = _stream.stream_events(_stub_client_model(), "POST", "http://x")
    # Consume a few events from a stream that never sends EOF, then stop.
    got = await _collect(agen, 5)
    assert len(got) == 5
    assert got[0] == ("message", '{"n": 0}')
    # aclose() must run the finally block and close the underlying connection.
    await agen.aclose()
    assert stream.closed is True


# --- connect errors ------------------------------------------------------------


async def test_connect_401_raises_core_api_error(monkeypatch):
    body = b'{"code": 401, "message": "unauthorized", "details": ["nope"]}'
    _patch(monkeypatch, _client(status=401, content_type="application/json", body=body))
    with pytest.raises(CoreAPIError) as exc:
        async for _ in _stream.stream_events(_stub_client_model(), "POST", "http://x"):
            pass
    assert exc.value.code == 401


async def test_connect_error_without_json_body(monkeypatch):
    _patch(monkeypatch, _client(status=500, content_type="text/plain", body=b"boom"))
    with pytest.raises(CoreAPIError) as exc:
        async for _ in _stream.stream_events(_stub_client_model(), "POST", "http://x"):
            pass
    assert exc.value.code == 500


# --- stream endpoint methods on AsyncClient -----------------------------------


def test_stream_methods_are_async_only():
    from core_client import AsyncClient, Client

    for name in ("v3_events_stream", "v3_cluster_events_stream", "v3_cluster_events_process_stream"):
        assert hasattr(AsyncClient, name)
        assert not hasattr(Client, name)


def _client_capturing(captured, lines):
    def handler(request):
        captured["url"] = str(request.url)
        captured["body"] = request.content
        return httpx.Response(
            200,
            headers={"content-type": "application/x-json-stream"},
            stream=_MockStream(lines),
        )

    return httpx.AsyncClient(transport=httpx.MockTransport(handler), http2=False)


async def test_process_stream_method_end_to_end(monkeypatch):
    from core_client import AsyncClient
    from core_client.base.models.v3 import EventFilters, ProcessEventFilter

    captured = {}
    lines = [b'{"pid":"p1","type":"progress"}\n', b'{"pid":"p2","type":"progress"}\n']
    _patch(monkeypatch, _client_capturing(captured, lines))

    client = AsyncClient(base_url="http://h")
    out = []
    async for ev in client.v3_cluster_events_process_stream(
        filters=EventFilters(filters=[ProcessEventFilter(type="progress")])
    ):
        out.append(ev)

    import json

    assert captured["url"].endswith("/api/v3/cluster/events/process")
    assert json.loads(captured["body"]) == {"filters": [{"type": "progress"}]}
    assert out == [
        ("message", '{"pid":"p1","type":"progress"}'),
        ("message", '{"pid":"p2","type":"progress"}'),
    ]


async def test_stream_method_typed_model(monkeypatch):
    from core_client import AsyncClient
    from core_client.base.models.v3 import LogEvent

    captured = {}
    lines = [b'{"event":"start","level":6}\n']
    _patch(monkeypatch, _client_capturing(captured, lines))

    client = AsyncClient(base_url="http://h")
    out = [ev async for ev in client.v3_events_stream(model=LogEvent)]
    assert out[0][0] == "message"
    assert isinstance(out[0][1], LogEvent)
    assert out[0][1].event == "start"


# --- throughput (Aufgabe 6) ----------------------------------------------------


@pytest.mark.slow
async def test_raw_mode_throughput(monkeypatch):
    # A busy cluster emits >800 process events/s; the raw generator loop must not
    # be the bottleneck. This measures the generator's own overhead over a mock
    # stream (no network, no per-event validation).
    n_lines = 20000
    line = b'{"pid":"p","domain":"d","type":"progress"}\n'
    _patch(
        monkeypatch,
        _client(content_type="application/x-json-stream", stream=_MockStream([line] * n_lines)),
    )
    t0 = time.monotonic()
    count = 0
    async for _ in _stream.stream_events(_stub_client_model(), "POST", "http://x"):
        count += 1
    elapsed = time.monotonic() - t0
    rate = count / elapsed if elapsed else float("inf")
    assert count == n_lines
    assert rate >= 800, f"throughput {rate:.0f}/s below 800/s floor"
