import httpx
from ._http import execute_async, execute_sync
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import Process


@validate_call()
def _build_request(
    client: Client,
    id: str,
    filter: str = "",
    reference: str = "",
    process_ids: str = "",
    idpattern: str = "",
    refpattern: str = "",
    ownerpattern: str = "",
    domainpattern: str = "",
    retries: int = None,
    timeout: float = None,
):
    """
    Args:
        id (str): ID of the node
        filter (str): config, state, report, metadata
        reference (str): reference value
        process_ids (str): Comma separated list of process ids. Sent as the `id`
            query parameter; renamed here because `id` is the node.
        idpattern (str): Glob pattern for ids
        refpattern (str): Glob pattern for references
        ownerpattern (str): Glob pattern for owners
        domainpattern (str): Glob pattern for domains
    """
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "get",
        "url": f"{client.base_url}/api/v3/cluster/node/{id}/process?filter={filter}&reference={reference}&id={process_ids}&idpattern={idpattern}&refpattern={refpattern}&ownerpattern={ownerpattern}&domainpattern={domainpattern}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": None,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        response_200 = TypeAdapter(list[Process]).validate_python(response.json())
        return response_200
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
