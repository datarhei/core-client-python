"""Request-building unit tests for cluster endpoints that cannot be exercised
against a standalone Core (they require a real cluster). These cover the
modules added/fixed per CLIENT-TODO §1 and §1a without needing a backend.
"""

import pytest

from core_client import Client
from core_client.base.api import (
    v3_cluster_db_get_process_map,
    v3_cluster_fs_get_file_list,
    v3_cluster_get_deployments,
    v3_cluster_get_healthy,
    v3_cluster_process_get_metadata,
    v3_cluster_process_get_probe,
)
from core_client.base.models.v3 import ClusterDeployments
from core_client.models import Client as ClientModel


@pytest.fixture
def client_model():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


def test_new_cluster_methods_are_registered():
    client = Client(base_url="http://example.com")
    for name in [
        "v3_cluster_get_healthy",
        "v3_cluster_get_deployments",
        "v3_cluster_process_get_metadata",
        "v3_cluster_db_get_process_map",
        "v3_cluster_fs_get_file_list",
    ]:
        assert hasattr(client, name), name


def test_cluster_get_healthy_request(client_model):
    request, _ = v3_cluster_get_healthy._build_request(client_model)
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/healthy"


def test_cluster_get_deployments_request(client_model):
    request, _ = v3_cluster_get_deployments._build_request(client_model)
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/deployments"


def test_cluster_process_get_metadata_request(client_model):
    request, _ = v3_cluster_process_get_metadata._build_request(
        client_model, id="p1", key="k", domain="d"
    )
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/process/p1/metadata/k?domain=d"


def test_cluster_db_get_process_map_request(client_model):
    request, _ = v3_cluster_db_get_process_map._build_request(client_model)
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/db/map/process"


def test_cluster_fs_get_file_list_request(client_model):
    request, _ = v3_cluster_fs_get_file_list._build_request(
        client_model, storage="mem", glob="*.ts", sort="name", order="asc"
    )
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/fs/mem?glob=*.ts&sort=name&order=asc"


def test_cluster_process_get_probe_uses_get(client_model):
    # §1a regression guard: this endpoint must use GET, not POST.
    request, _ = v3_cluster_process_get_probe._build_request(client_model, id="p1", domain="d")
    assert request["method"] == "get"
    assert request["url"] == "http://h/api/v3/cluster/process/p1/probe?domain=d"


def test_cluster_deployments_model_parses():
    parsed = ClusterDeployments.model_validate(
        {"process": [{"action": "relocate", "id": "x", "node_id": "n1"}]}
    )
    assert parsed.process[0].action.value == "relocate"
