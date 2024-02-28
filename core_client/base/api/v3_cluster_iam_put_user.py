import httpx
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import IamUser


@validate_call()
def _build_request(
    client: Client,
    name: str,
    config: IamUser,
    domain: str = "",
    retries: int = None,
    timeout: float = None,
):
    """_summary_
    Args:
        domain (str): Domain of the acting user
    """
    if not isinstance(config, dict):
        config = config.dict(exclude_none=True)
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "put",
        "url": f"{client.base_url}/api/v3/cluster/iam/user/{name}?domain={domain}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": config,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        response_200 = TypeAdapter(IamUser).validate_python(response.json())
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
