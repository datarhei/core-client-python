"""Streaming endpoint: ``POST /api/v3/events``.

Endless SSE stream of media events. Registered on ``AsyncClient`` as an
async-generator method (see ``_add_stream_method``).
"""

from ...models import Client
from ._stream import serialize_filters, stream_events


def _build_request(client: Client, filters=None):
    return "POST", f"{client.base_url}/api/v3/events", serialize_filters(filters)


async def asyncio_stream(client: Client, *, filters=None, frame: bool = True, model=None):
    method, url, body = _build_request(client, filters=filters)
    async for item in stream_events(client, method, url, json=body, frame=frame):
        if model is not None and frame:
            event_type, data = item
            yield event_type, model.model_validate_json(data)
        else:
            yield item
