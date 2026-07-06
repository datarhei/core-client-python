"""Unit tests for the endpoints added from the core-openapi.json route audit,
plus regression guards for two HTTP-method fixes. Most target cluster/newer-Core
routes that cannot be exercised against a standalone Core, so we assert request
construction without a backend.
"""

import pathlib

import pytest

from core_client import Client
from core_client.base.api import (
    graph_query,
    v3_cluster_db_get_kv,
    v3_cluster_db_get_node_list,
    v3_cluster_db_get_process,
    v3_cluster_db_get_reallocate_map,
    v3_cluster_get_snapshot,
    v3_cluster_post_events,
    v3_cluster_put_transfer,
    v3_events_post,
    v3_events_post_media,
    v3_fs_delete_file_list,
    v3_process_post_validate,
    v3_process_put_report,
)
from core_client.base.models.v3 import (
    ClusterStoreNode,
    GraphResponse,
    LogEvent,
    MediaEvent,
)
from core_client.models import Client as ClientModel

API_DIR = pathlib.Path("core_client/base/api")
CONFIG = {"id": "x", "reference": "r", "options": [], "input": [], "output": []}
REPORT = {"created_at": 0, "prelude": [], "log": []}
FILTERS = {"filters": []}


@pytest.fixture
def cm():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


NEW_METHODS = [
    "v3_fs_delete_file_list",
    "v3_process_post_validate",
    "v3_process_put_report",
    "v3_cluster_db_get_kv",
    "v3_cluster_db_get_reallocate_map",
    "v3_cluster_db_get_node_list",
    "v3_cluster_db_get_process",
    "v3_cluster_post_events",
    "v3_cluster_get_snapshot",
    "v3_cluster_put_transfer",
    "v3_events_post",
    "v3_events_post_media",
    "graph_query",
]


def test_new_methods_registered():
    client = Client(base_url="http://example.com")
    for name in NEW_METHODS:
        assert hasattr(client, name), name


def test_request_construction(cm):
    cases = [
        (v3_fs_delete_file_list._build_request(cm, storage="mem", glob="*.ts"), "delete",
         "http://h/api/v3/fs/mem?glob=*.ts&size_min=&size_max=&lastmod_start=&lastmod_end="),
        (v3_process_post_validate._build_request(cm, config=CONFIG), "post",
         "http://h/api/v3/process/validate"),
        (v3_process_put_report._build_request(cm, id="p", report=REPORT, domain="d"), "put",
         "http://h/api/v3/process/p/report?domain=d"),
        (v3_cluster_db_get_kv._build_request(cm), "get", "http://h/api/v3/cluster/db/kv"),
        (v3_cluster_db_get_reallocate_map._build_request(cm), "get",
         "http://h/api/v3/cluster/db/map/reallocate"),
        (v3_cluster_db_get_node_list._build_request(cm), "get", "http://h/api/v3/cluster/db/node"),
        (v3_cluster_db_get_process._build_request(cm, id="p1", domain="d"), "get",
         "http://h/api/v3/cluster/db/process/p1?domain=d"),
        (v3_cluster_post_events._build_request(cm, filters=FILTERS), "post",
         "http://h/api/v3/cluster/events"),
        (v3_cluster_get_snapshot._build_request(cm), "get", "http://h/api/v3/cluster/snapshot"),
        (v3_cluster_put_transfer._build_request(cm, id="n1"), "put",
         "http://h/api/v3/cluster/transfer/n1"),
        (v3_events_post._build_request(cm, filters=FILTERS), "post", "http://h/api/v3/events"),
        (v3_events_post_media._build_request(cm, type="video", glob="*"), "post",
         "http://h/api/v3/events/media/video?glob=*"),
        (graph_query._build_request(cm, query={"query": "{ping}"}), "post",
         "http://h/api/graph/query"),
    ]
    for (request, _), method, url in cases:
        assert request["method"] == method, (request["method"], url)
        assert request["url"] == url


@pytest.mark.parametrize(
    "module,expected_method",
    [
        ("v3_cluster_put_reallocation", "put"),
        ("v3_process_put_playout_input_stream", "put"),
    ],
)
def test_method_bug_fixes(module, expected_method):
    # Regression guard: these modules previously used GET (copy-paste bug).
    text = (API_DIR / f"{module}.py").read_text()
    assert f'"method": "{expected_method}"' in text
    assert '"method": "get"' not in text


def test_cluster_reallocation_body_serializes_as_array(cm):
    # Regression: ClusterReallocation must be a RootModel[list[...]], so the
    # body is a top-level array, not {"RootModel": {...}}.
    from core_client.base.api import v3_cluster_put_reallocation
    from core_client.base.models.v3 import ClusterReallocation

    payload = [{"target_node_id": "n1", "process_ids": [{"id": "p1", "domain": "d"}]}]
    assert ClusterReallocation.model_validate(payload).model_dump() == payload

    request, _ = v3_cluster_put_reallocation._build_request(cm, reallocation=payload)
    assert request["method"] == "put"
    assert request["json"] == payload


def test_models_parse():
    assert ClusterStoreNode.model_validate({"id": "n1", "state": "online"}).id == "n1"
    assert LogEvent.model_validate({"event": "start", "level": 6, "ts": 1}).level == 6
    assert MediaEvent.model_validate({"action": "add", "names": ["a", "b"]}).names == ["a", "b"]
    assert GraphResponse.model_validate({"data": {"x": 1}, "errors": []}).data == {"x": 1}
