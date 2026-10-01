"""Async streaming helper for the event endpoints.

The Core event endpoints are endless streams in two wire formats:

* ``text/event-stream`` (SSE) — ``event:``/``data:`` lines, ``:keepalive`` comments,
  blank lines separating events;
* ``application/x-json-stream`` (NDJSON) — one raw JSON object per line.

``stream_events`` consumes either as an async generator, event by event, without a
read timeout (the connect timeout stays finite).

Notes / live findings:

* **HTTP/1.1 only.** The Core cluster terminates HTTP/2 stream connections
  immediately (GOAWAY), so this uses a dedicated ``httpx.AsyncClient(http2=False)``
  instead of the pooled HTTP/2 client.
* No Pydantic validation happens per line — this runs on a hot path (a busy cluster
  emits thousands of events per second). Typed parsing is opt-in at the call site.
* **NDJSON is requested by default** (``accept``). The log-event endpoints serve
  either format and default to SSE, but Core's SSE branch is broken for a cluster:
  ``cluster_events.go`` calls ``LogEvent.Unmarshal(e)`` and ignores its return
  value, and since the cluster proxy delivers ``*api.LogEventRaw`` - for which
  Unmarshal bails out without touching the struct - the zero value is serialized.
  The stream then consists of ``{"ts":0,"level":"","event":"", ...}`` with an empty
  SSE event name. Its NDJSON branch decodes the raw payload correctly. The process
  endpoints ignore ``Accept`` and always serve NDJSON.
"""

import httpx

from ...exceptions import CoreAPIError
from ..models import Error

#: Wire formats the Core event endpoints can serve.
NDJSON = "application/x-json-stream"
SSE = "text/event-stream"

#: The exact keepalive lines Core writes on the NDJSON streams, one per endpoint
#: family (log / process / media). They are transport noise, not events - Core
#: itself drops inbound keepalives before filtering - and the SSE framing hides
#: them as ``:keepalive`` comments, so framed mode drops them as well. Raw mode
#: (``frame=False``) still yields them, like it yields the SSE comments.
_NDJSON_KEEPALIVES = frozenset(
    {
        '{"event": "keepalive"}',
        '{"type":"keepalive"}',
        '{"action":"keepalive"}',
    }
)


def _make_stream_client():
    """Return the httpx client used for streaming.

    Isolated so tests can monkeypatch it with a ``MockTransport``-backed client.
    """
    return httpx.AsyncClient(http2=False)


def serialize_filters(filters):
    """Normalize a filter argument to a JSON body.

    Accepts an ``EventFilters`` (or any pydantic model), a raw ``dict``
    (passed through for backwards compatibility), or ``None``.

    ``None`` becomes an empty filter set rather than no body at all: the event
    endpoints reject a bodyless request with ``400`` ("request doesn't contain any
    content", see ``ShouldBindJSONValidation``), while an empty filter list is how
    Core expresses "deliver everything".
    """
    if filters is None:
        return {"filters": []}
    if isinstance(filters, dict):
        return filters
    return filters.model_dump(exclude_none=True)


def _connect_error(response, body: bytes) -> CoreAPIError:
    try:
        error = Error.model_validate_json(body)
    except Exception:
        reason = response.reason_phrase or "Error"
        detail = body.decode(errors="replace")[:200] or reason
        error = Error(code=response.status_code, message=reason, details=[detail])
    return CoreAPIError(error)


async def stream_events(
    client, method: str, url: str, *, json=None, frame: bool = True, accept: str = NDJSON
):
    """Yield events from an endless Core event stream.

    ``frame=True``  -> yield ``(event_type: str, data: str)`` (SSE interpreted,
                       raw NDJSON lines delivered as ``("message", line)``).
    ``frame=False`` -> yield each raw line as ``str``.

    ``accept`` selects the wire format. It defaults to ``NDJSON`` (see the module
    docstring for why); pass ``SSE`` to get the server-sent-events framing, where
    the yielded ``event_type`` is the event's component instead of ``"message"``.

    A non-200 on connect is raised as ``CoreAPIError`` (regardless of
    ``raise_on_error``) so callers can distinguish e.g. 401 for a targeted refresh.
    Network errors propagate as ``httpx`` exceptions. On EOF the generator ends
    normally. Cancellation / ``aclose()`` closes the connection cleanly.
    """
    timeout = httpx.Timeout(connect=client.timeout, read=None, write=None, pool=None)
    # Replace any case variant of `accept` rather than adding a second header -
    # which format Core picks when it receives both is undefined.
    headers = {k: v for k, v in client.headers.items() if k.lower() != "accept"}
    headers["accept"] = accept
    stream_client = _make_stream_client()
    try:
        async with stream_client.stream(
            method, url, headers=headers, json=json, timeout=timeout
        ) as response:
            if response.status_code != 200:
                raise _connect_error(response, await response.aread())

            event_type = "message"
            async for line in response.aiter_lines():
                if not line:
                    event_type = "message"
                    continue
                if not frame:
                    yield line
                    continue
                if line.startswith(":"):
                    continue  # SSE comment / keepalive
                if line.startswith("event:"):
                    event_type = line[len("event:") :].strip()
                    continue
                if line.startswith("data:"):
                    yield event_type, line[len("data:") :].lstrip()
                    continue
                stripped = line.strip()
                if stripped[:1] in ("{", "["):
                    if stripped in _NDJSON_KEEPALIVES:
                        continue
                    yield event_type, line  # raw NDJSON object/array
                    event_type = "message"
                    continue
                # other SSE fields (id:, retry:, ...) are ignored
    finally:
        await stream_client.aclose()
