import httpx
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import FilesystemOperationOrder


@validate_call()
def _build_request(
    client: Client,
    source: str,
    target: str,
    operation: FilesystemOperationOrder,
    bandwidth_limit_kbit: int = None,
    retries: int = None,
    timeout: float = None,
):
    data = {
        "source": source,
        "operation": operation,
        "target": target,
        "bandwidth_limit_kbit": bandwidth_limit_kbit,
    }
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "put",
        "url": f"{client.base_url}/api/v3/fs",
        "headers": client.headers,
        "timeout": timeout,
        "content": None,
        "json": data,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    else:
        response_error = TypeAdapter(Error).validate_python(response.json())
        return response_error


def sync(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    transport = httpx.HTTPTransport(retries=retries)
    httpx_client = httpx.Client(transport=transport, http2=True)
    response = httpx_client.request(**request)
    return _build_response(response=response)


async def asyncio(client: Client, **kwargs):
    request, retries = _build_request(client, **kwargs)
    transport = httpx.AsyncHTTPTransport(retries=retries)
    async with httpx.AsyncClient(transport=transport) as httpx_client:
        response = await httpx_client.request(**request)
    return _build_response(response=response)
