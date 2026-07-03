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
    link: str,
    retries: int = None,
    timeout: float = None,
):
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "patch",
        "url": f"{client.base_url}/api/v3/fs/{storage}/{path}",
        "headers": client.headers,
        "timeout": timeout,
        "content": None,
        "json": link,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 201:
        if response.headers["content-type"] == "application/json; charset=UTF-8":
            response_201 = response.json()
        else:
            response_201 = response.text
        return response_201
    elif response.status_code == 204:
        if response.headers["content-type"] == "application/json; charset=UTF-8":
            response_204 = response.json()
        else:
            response_204 = response.text
        return response_204
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
