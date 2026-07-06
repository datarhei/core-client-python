"""Regression tests for endpoints whose 200 response is a string per the
OpenAPI schema but was wrongly parsed into a model.
"""

import httpx

from core_client.base.api import v3_cluster_node_put_state, v3_iam_delete_user
from core_client.base.models import Error


def test_node_put_state_returns_string():
    # openapi: PUT /api/v3/cluster/node/{id}/state -> 200 string
    assert v3_cluster_node_put_state._build_response(httpx.Response(200, json="OK")) == "OK"


def test_iam_delete_user_returns_string():
    # openapi: DELETE /api/v3/iam/user/{name} -> 200 string
    assert v3_iam_delete_user._build_response(httpx.Response(200, json="OK")) == "OK"


def test_string_endpoints_still_return_error_on_failure():
    err = {"code": 404, "message": "Not Found", "details": ["Not Found"]}
    for module in (v3_cluster_node_put_state, v3_iam_delete_user):
        res = module._build_response(httpx.Response(404, json=err))
        assert isinstance(res, Error)
        assert res.code == 404
