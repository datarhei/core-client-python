import pytest

from core_client import Client
from core_client.base.models import About

from .conftest import CLIENT_TIMEOUT

pytestmark = pytest.mark.integration


def test_ping(core_url):
    client = Client(base_url=core_url, username="", password="", timeout=CLIENT_TIMEOUT)
    assert client.ping() == "pong"


def test_about_reports_supported_version(admin_client):
    res = admin_client.about()
    assert isinstance(res, About)
    assert isinstance(res.name, str)
    # requires core v10.10+
    major, minor, *_ = res.version.number.split(".")
    assert (int(major), int(minor)) >= (10, 10)
