import os

import pytest

from core_client import Client
from core_client.base.models import Error, Token
from core_client.base.models.v3 import (
    Cluster,
    ClusterNode,
    ClusterNodeState,
    ClusterNodeVersion,
)

pytestmark = pytest.mark.integration

core_url_1 = os.getenv("CORE_URL_1", "http://127.0.0.1:8080")
core_url_2 = os.getenv("CORE_URL_2", "http://127.0.0.1:8081")
client_1 = Client(base_url=f"{core_url_1}", username="", password="")
client_2 = Client(base_url=f"{core_url_2}", username="", password="")


def _get_first_node_id(client: Client) -> str:
    res = client.v3_cluster_node_get_list()
    if isinstance(res, Error):
        pytest.skip("Cluster node list is not available")
    if len(res) == 0:
        pytest.skip("No cluster nodes returned")
    return res[0].id


def test_prepare():
    res_1 = client_1.login()
    res_2 = client_2.login()
    assert isinstance(res_1, Token)
    assert isinstance(res_2, Token)


def test_v3_cluster_get():
    res_1 = client_1.v3_cluster_get()
    res_2 = client_2.v3_cluster_get()
    assert isinstance(res_1, Cluster)
    assert isinstance(res_2, Cluster)


def test_v3_cluster_node_get_list():
    res = client_1.v3_cluster_node_get_list()
    assert isinstance(res, list)
    if res:
        assert isinstance(res[0], ClusterNode)


def test_v3_cluster_node_get_unknown():
    res = client_1.v3_cluster_node_get(id="unknown")
    assert isinstance(res, Error)


def test_v3_cluster_node_get_existing():
    node_id = _get_first_node_id(client_1)
    res = client_1.v3_cluster_node_get(id=node_id)
    assert isinstance(res, ClusterNode)


def test_v3_cluster_node_get_state_unknown():
    res = client_1.v3_cluster_node_get_state(id="unknown")
    assert isinstance(res, Error)


def test_v3_cluster_node_get_state_existing():
    node_id = _get_first_node_id(client_1)
    res = client_1.v3_cluster_node_get_state(id=node_id)
    assert isinstance(res, ClusterNodeState)


def test_v3_cluster_node_get_version_existing():
    node_id = _get_first_node_id(client_1)
    res = client_1.v3_cluster_node_get_version(id=node_id)
    assert isinstance(res, ClusterNodeVersion)
