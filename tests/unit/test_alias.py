"""Tests for the alias endpoints (GET/PUT/POST /api/v3/alias, GET/PUT/DELETE
/api/v3/alias/rule and their /api/v3/cluster/alias counterparts) and for the
`reason` of process commands. Request construction is asserted without a backend.
"""

import importlib
import json
from types import SimpleNamespace

import httpx
import pytest

from core_client import AsyncClient, Client
from core_client.base.api import _http
from core_client.base.models.v3 import Alias, ProcessCommand
from core_client.models import Client as ClientModel

# A realistic pattern: `+` would arrive as a space and `?`/`&`/`#` would break
# the query string if the client did not percent-encode it.
PATTERN = r"^/live/(?P<name>.+)\.m3u8$&x=#1"
ALIAS = {"pattern": PATTERN, "target": "/memfs/${name}/index.m3u8"}

SUFFIXES = ["get_list", "put_list", "post", "get", "put", "delete"]
PREFIXES = {"v3_alias": "/api/v3/alias", "v3_cluster_alias": "/api/v3/cluster/alias"}


@pytest.fixture
def cm():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


def _mod(name):
    return importlib.import_module(f"core_client.base.api.{name}")


@pytest.mark.parametrize("prefix", PREFIXES)
def test_alias_methods_registered(prefix):
    for suffix in SUFFIXES:
        name = f"{prefix}_{suffix}"
        assert hasattr(Client, name), name
        assert hasattr(AsyncClient, name), name


@pytest.mark.parametrize("prefix,base", PREFIXES.items())
def test_alias_request_construction(cm, prefix, base):
    quoted = "%5E%2Flive%2F%28%3FP%3Cname%3E.%2B%29%5C.m3u8%24%26x%3D%231"
    cases = {
        "get_list": ({}, "get", base, None),
        "put_list": ({"aliases": [ALIAS]}, "put", base, [ALIAS]),
        "post": ({"alias": ALIAS}, "post", base, ALIAS),
        "get": ({"pattern": PATTERN}, "get", f"{base}/rule?pattern={quoted}", None),
        "put": ({"pattern": PATTERN, "alias": ALIAS}, "put", f"{base}/rule?pattern={quoted}", ALIAS),
        "delete": ({"pattern": PATTERN}, "delete", f"{base}/rule?pattern={quoted}", None),
    }
    for suffix, (kwargs, method, path, body) in cases.items():
        request, _ = _mod(f"{prefix}_{suffix}")._build_request(cm, **kwargs)
        assert request["method"] == method, suffix
        assert request["url"] == f"http://h{path}", suffix
        assert request["json"] == body, suffix


def test_pattern_survives_the_wire():
    # Send the request through a real httpx client and check what a server sees:
    # the decoded query value must be the exact pattern, and the raw query must
    # carry `+` as %2B (Go's query parser turns a literal `+` into a space).
    seen = {}

    def handler(request):
        seen["pattern"] = request.url.params["pattern"]
        seen["raw"] = request.url.query.decode()
        return httpx.Response(200, json=ALIAS)

    stub = SimpleNamespace(retries=3, http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    request, retries = _mod("v3_alias_get")._build_request(
        ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0), pattern=PATTERN
    )
    response = _http.execute_sync(stub, request, retries)

    assert seen["pattern"] == PATTERN
    assert "%2B" in seen["raw"] and "+" not in seen["raw"]
    assert _mod("v3_alias_get")._build_response(response) == Alias(**ALIAS)


def test_alias_responses_are_parsed():
    lst = httpx.Response(200, json=[ALIAS])
    one = httpx.Response(200, json=ALIAS)
    ok = httpx.Response(200, json="OK")
    conflict = httpx.Response(409, json={"code": 409, "message": "Conflict", "details": ["exists"]})

    assert _mod("v3_alias_get_list")._build_response(lst) == [Alias(**ALIAS)]
    assert _mod("v3_cluster_alias_put_list")._build_response(lst) == [Alias(**ALIAS)]
    assert _mod("v3_alias_post")._build_response(one).target == ALIAS["target"]
    assert _mod("v3_cluster_alias_delete")._build_response(ok) == "OK"
    assert _mod("v3_alias_post")._build_response(conflict).code == 409


def test_alias_model_requires_both_fields():
    with pytest.raises(Exception):
        Alias(pattern="^/x$")


# --- process command reason -------------------------------------------------------


@pytest.mark.parametrize(
    "module,path",
    [
        ("v3_process_put_command", "/api/v3/process/p1/command"),
        ("v3_cluster_process_put_command", "/api/v3/cluster/process/p1/command"),
    ],
)
def test_command_reason(cm, module, path):
    mod = _mod(module)

    request, _ = mod._build_request(cm, id="p1", command="stop", reason="maintenance")
    assert request["url"] == f"http://h{path}?domain="
    assert json.loads(json.dumps(request["json"])) == {"command": "stop", "reason": "maintenance"}

    # Without a reason the body stays exactly as before.
    request, _ = mod._build_request(cm, id="p1", command="restart")
    assert json.loads(json.dumps(request["json"])) == {"command": "restart"}


def test_process_command_model_has_reason():
    assert ProcessCommand(command="stop", reason="r").reason == "r"
    assert ProcessCommand(command="stop").reason is None
