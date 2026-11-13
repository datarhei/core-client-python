import httpx
from ._http import execute_async, execute_sync
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import Alias


@validate_call()
def _build_request(
    client: Client,
    aliases: list[Alias],
    retries: int = None,
    timeout: float = None,
):
    payload = []
    for alias in aliases:
        if not isinstance(alias, dict):
            payload.append(alias.model_dump())
        else:
            payload.append(alias)
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "put",
        "url": f"{client.base_url}/api/v3/alias",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": payload,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        return TypeAdapter(list[Alias]).validate_python(response.json())
    else:
        response_error = TypeAdapter(Error).validate_python(response.json())
        return response_error


def sync(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    response = execute_sync(client, request, retries)
    return _build_response(response=response)


async def asyncio(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    response = await execute_async(client, request, retries)
    return _build_response(response=response)
