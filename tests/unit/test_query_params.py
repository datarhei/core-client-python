"""Query parameters that existing endpoints were missing, found by comparing every
operation's query parameters against the Core OpenAPI doc and the Core handlers.
"""

import pytest

from core_client.base.api import (
    v3_cluster_iam_get_user_list,
    v3_cluster_node_get_process_list,
    v3_iam_post_user,
    v3_process_delete,
)
from core_client.models import Client as ClientModel

USER = {"name": "u1"}


@pytest.fixture
def cm():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


def test_process_delete_purge(cm):
    # Core defaults purge to true; the client used to have no way to turn it off.
    def url(**kw):
        return v3_process_delete._build_request(cm, id="p1", **kw)[0]["url"]

    assert url() == "http://h/api/v3/process/p1?domain=&purge=true"
    assert url(purge=False, domain="d") == "http://h/api/v3/process/p1?domain=d&purge=false"


def test_cluster_node_process_list_filters(cm):
    request, _ = v3_cluster_node_get_process_list._build_request(
        cm, id="node1", filter="state", reference="r", process_ids="p1,p2",
        idpattern="p*", refpattern="r*", ownerpattern="o*", domainpattern="d*",
    )
    assert request["url"] == (
        "http://h/api/v3/cluster/node/node1/process?filter=state&reference=r&id=p1,p2"
        "&idpattern=p*&refpattern=r*&ownerpattern=o*&domainpattern=d*"
    )


def test_cluster_node_process_list_without_filters(cm):
    request, _ = v3_cluster_node_get_process_list._build_request(cm, id="node1")
    assert request["url"].startswith("http://h/api/v3/cluster/node/node1/process?")
    # Empty values are treated as absent by Core (util.DefaultQuery).
    assert "id=&" in request["url"]


def test_iam_domain_params(cm):
    assert v3_cluster_iam_get_user_list._build_request(cm, domain="d")[0]["url"] == (
        "http://h/api/v3/cluster/iam/user?domain=d"
    )
    request, _ = v3_iam_post_user._build_request(cm, config=USER, domain="d")
    assert request["url"] == "http://h/api/v3/iam/user?domain=d"
    assert request["json"]["name"] == "u1"
