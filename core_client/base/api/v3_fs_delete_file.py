import httpx
from pydantic import parse_obj_as, validate_arguments

from ...models import Client
from ..models import Error


@validate_arguments()
def _build_request(
    client: Client,
    name: str,
    path: str,
    retries: int = None,
    timeout: float = None,
):
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "delete",
        "url": f"{client.base_url}/api/v3/fs/{name}/{path}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": None,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        if (
            response.headers["content-type"]
            == "application/json; charset=UTF-8"
        ):
            response_200 = response.json()
        else:
            response_200 = response.text
        return response_200
    else:
        response_error = parse_obj_as(Error, response.json())
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
