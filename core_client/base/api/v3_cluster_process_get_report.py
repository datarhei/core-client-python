import httpx
from ._http import execute_async, execute_sync
from pydantic import TypeAdapter, validate_call

from ...models import Client
from ..models import Error
from ..models.v3 import ProcessReport

# NOTE: Core's OpenAPI annotation for this route says `api.ProcessState`, but the
# handler returns `process.Report` (http/handler/api/cluster_process.go), i.e. an
# api.ProcessReport - same as the non-cluster GET /api/v3/process/{id}/report.


@validate_call()
def _build_request(
    client: Client,
    id: str,
    created_at: int = "",
    exited_at: int = "",
    domain: str = "",
    retries: int = None,
    timeout: float = None,
):
    if not retries:
        retries = client.retries
    if not timeout:
        timeout = client.timeout
    return {
        "method": "get",
        "url": f"{client.base_url}/api/v3/cluster/process/{id}/report?domain={domain}&created_at={created_at}&exited_at={exited_at}",
        "headers": client.headers,
        "timeout": timeout,
        "data": None,
        "json": None,
    }, retries


def _build_response(response: httpx.Response):
    if response.status_code == 200:
        response_200 = TypeAdapter(ProcessReport).validate_python(response.json())
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
