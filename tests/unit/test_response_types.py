"""Regression tests for endpoints whose 200 response is a string per the
OpenAPI schema but was wrongly parsed into a model.
"""

import httpx

from core_client.base.api import (
    v3_cluster_node_put_state,
    v3_iam_delete_user,
    v3_process_get_playout_input_status,
)
from core_client.base.models import Error
from core_client.base.models.v3 import PlayoutStatus, PlayoutStatusIO, PlayoutStatusSwap


def test_node_put_state_returns_string():
    # openapi: PUT /api/v3/cluster/node/{id}/state -> 200 string
    assert v3_cluster_node_put_state._build_response(httpx.Response(200, json="OK")) == "OK"


def test_iam_delete_user_returns_string():
    # openapi: DELETE /api/v3/iam/user/{name} -> 200 string
    assert v3_iam_delete_user._build_response(httpx.Response(200, json="OK")) == "OK"


def test_playout_input_status_returns_typed_model():
    # openapi: GET .../playout/{input_id}/status -> 200 api.PlayoutStatus
    sample = {
        "id": "in",
        "input": {"packet": 5, "size_kb": 100, "state": "running", "time": 42},
        "swap": {"status": "ok", "url": "u"},
        "debug": {"x": 1},
    }
    res = v3_process_get_playout_input_status._build_response(httpx.Response(200, json=sample))
    assert isinstance(res, PlayoutStatus)
    assert isinstance(res.input, PlayoutStatusIO)
    assert isinstance(res.swap, PlayoutStatusSwap)
    assert res.input.state == "running"
    assert res.debug == {"x": 1}


def test_string_endpoints_still_return_error_on_failure():
    err = {"code": 404, "message": "Not Found", "details": ["Not Found"]}
    for module in (v3_cluster_node_put_state, v3_iam_delete_user):
        res = module._build_response(httpx.Response(404, json=err))
        assert isinstance(res, Error)
        assert res.code == 404
