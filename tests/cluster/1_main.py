import os

from core_client import Client
from core_client.base.models import Token, Error
from core_client.base.models.v3 import ClusterNodeList, ClusterNode, ClusterNodeAuth

core_url_1 = os.getenv("CORE_URL_1", "http://127.0.0.1:8080")
core_url_2 = os.getenv("CORE_URL_2", "http://127.0.0.1:8081")
client_1 = Client(base_url=f"{core_url_1}", username="", password="")
client_2 = Client(base_url=f"{core_url_2}", username="", password="")


def test_prepare():
    res_1 = client_1.login()
    res_2 = client_2.login()
    assert type(res_1) is Token
    assert type(res_2) is Token


def test_v3_cluster_post_node():
    res_1 = client_1.v3_cluster_post_node(
        node=ClusterNodeAuth(address="http://10.0.0.1:80", username="", password="")
    )
    res_2 = client_1.v3_cluster_post_node(
        node=ClusterNodeAuth(address=f"{core_url_2}", username="", password="")
    )
    res_3 = client_2.v3_cluster_post_node(
        node=ClusterNodeAuth(address=f"{core_url_1}", username="", password="")
    )
    assert type(res_1) is Error
    assert type(res_2) is str
    assert type(res_3) is str


def test_v3_cluster_get_list():
    res = client_1.v3_cluster_get_list()
    assert type(res) is ClusterNodeList


def test_v3_cluster_get_node():
    node_list = client_1.v3_cluster_get_list()
    res_1 = client_1.v3_cluster_get_node(id="unknown")
    res_2 = client_1.v3_cluster_get_node(id=node_list[0].id)
    assert type(res_1) is Error
    assert type(res_2) is ClusterNode


def test_v3_cluster_put_node():
    node_list = client_1.v3_cluster_get_list()
    node = client_1.v3_cluster_get_node(id=node_list[0].id)
    # res_1 = client_1.v3_cluster_put_node(
    #     id="unknown", node=ClusterNodeAuth(address=f"{core_url_2}", username="", password="")
    # )
    res_2 = client_1.v3_cluster_put_node(
        id=node.id, node=ClusterNodeAuth(address="http://this.test:80", username="", password="")
    )
    res_3 = client_1.v3_cluster_put_node(
        id=node.id, node=ClusterNodeAuth(address=f"{core_url_2}", username="", password="")
    )
    # core issue
    # assert type(res_1) is Error
    assert type(res_2) is Error
    assert type(res_3) is str


def test_v3_cluster_get_node_proxy():
    # node_list = client_1.v3_cluster_get_list()
    res_1 = client_1.v3_cluster_get_node_proxy(id="unknown")
    # res_2 = client_1.v3_cluster_get_node_proxy(id=node_list[0].id)
    assert type(res_1) is Error
    # core issue
    # assert type(res_2) is list


def test_v3_cluster_delete_node():
    id_1 = client_1.about().id
    id_2 = client_2.about().id
    # res_1 = client_1.v3_cluster_delete_node(id="unknown")
    res_2 = client_1.v3_cluster_delete_node(id=id_2)
    res_3 = client_2.v3_cluster_delete_node(id=id_1)
    # core issue
    # assert type(res_1) is Error
    assert type(res_2) is str
    assert type(res_3) is str
