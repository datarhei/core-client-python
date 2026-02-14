from core_client import AsyncClient, AsyncMediaCoreClient, Client, MediaCoreClient
from core_client.base.models import Token as CoreToken
from datarhei.mediacore import AsyncMediaCoreClient as NamespaceAsyncMediaCoreClient
from datarhei.mediacore import MediaCoreClient as NamespaceMediaCoreClient
from datarhei.mediacore.base.models import Token as NamespaceToken


def test_new_class_names_alias_legacy_classes():
    assert MediaCoreClient is Client
    assert AsyncMediaCoreClient is AsyncClient


def test_new_namespace_points_to_client_classes():
    assert NamespaceMediaCoreClient is Client
    assert NamespaceAsyncMediaCoreClient is AsyncClient


def test_new_namespace_exposes_base_models():
    assert NamespaceToken is CoreToken

