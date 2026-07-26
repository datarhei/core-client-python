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
"""

import httpx

from ...exceptions import CoreAPIError
from ..models import Error


def _make_stream_client():
    """Return the httpx client used for streaming.

    Isolated so tests can monkeypatch it with a ``MockTransport``-backed client.
    """
    return httpx.AsyncClient(http2=False)


def serialize_filters(filters):
    """Normalize a filter argument to a JSON body.

    Accepts an ``EventFilters`` (or any pydantic model), a raw ``dict``
    (passed through for backwards compatibility), or ``None``.
    """
    if filters is None:
        return None
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


async def stream_events(client, method: str, url: str, *, json=None, frame: bool = True):
    """Yield events from an endless Core event stream.

    ``frame=True``  -> yield ``(event_type: str, data: str)`` (SSE interpreted,
                       raw NDJSON lines delivered as ``("message", line)``).
    ``frame=False`` -> yield each raw line as ``str``.

    A non-200 on connect is raised as ``CoreAPIError`` (regardless of
    ``raise_on_error``) so callers can distinguish e.g. 401 for a targeted refresh.
    Network errors propagate as ``httpx`` exceptions. On EOF the generator ends
    normally. Cancellation / ``aclose()`` closes the connection cleanly.
    """
    timeout = httpx.Timeout(connect=client.timeout, read=None, write=None, pool=None)
    stream_client = _make_stream_client()
    try:
        async with stream_client.stream(
            method, url, headers=client.headers, json=json, timeout=timeout
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
                stripped = line.lstrip()
                if stripped[:1] in ("{", "["):
                    yield event_type, line  # raw NDJSON object/array
                    event_type = "message"
                    continue
                # other SSE fields (id:, retry:, ...) are ignored
    finally:
        await stream_client.aclose()
