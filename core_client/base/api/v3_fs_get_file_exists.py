import httpx
from ._http import execute_async, execute_sync
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error


@validate_call()
def _build_request(
    client: Client,
    storage: str,
    path: str,
    retries: int = None,
    timeout: float = None,
):
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "head",
        "url": f"{client.base_url}/api/v3/fs/{storage}/{path}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": None,
    }, retries


def _build_response(response: httpx.Response):
    # This is a HEAD request: the body is always empty, so the useful
    # information (content-type, last-modified, ...) lives in the headers.
    if response.status_code in (200, 301):
        return dict(response.headers)
    elif response.content:
        response_error = TypeAdapter(Error).validate_python(response.json())
        return response_error
    else:
        # HEAD error responses carry no body, so synthesize it from the status.
        reason = response.reason_phrase or "Error"
        return Error(code=response.status_code, message=reason, details=[reason])


def sync(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    response = execute_sync(client, request, retries)
    return _build_response(response=response)


async def asyncio(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    response = await execute_async(client, request, retries)
    return _build_response(response=response)
