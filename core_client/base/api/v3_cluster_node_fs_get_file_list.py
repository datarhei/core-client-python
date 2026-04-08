import httpx
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import FilesystemFile


@validate_call()
def _build_request(
    client: Client,
    id: str,
    storage: str,
    glob: str = "",
    sort: str = "",
    order: str = "",
    retries: int = None,
    timeout: float = None,
):
    """_summary_
    Args:
        glob (str): glob pattern for file names
        sort (str): none, name, size or lastmod
        order (str): asc or desc
    """
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "get",
        "url": f"{client.base_url}/api/v3/cluster/node/{id}/fs/{storage}"
        + f"?glob={glob}"
        + f"&sort={sort}&order={order}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": None,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        response_200 = TypeAdapter(list[FilesystemFile]).validate_python(response.json())
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
