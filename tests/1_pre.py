import os
import time

import pytest

from core_client import Client
from core_client.base.models import About, Token
from core_client.base.models.v3 import ConfigSaved

pytestmark = pytest.mark.integration

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(base_url=f"{core_url}", username="", password="", timeout=20.0)


def test_ping():
    res = client.ping()
    assert isinstance(res, str)
    assert res == "pong"


def test_about():
    res = client.about()
    assert isinstance(res, About)
    assert isinstance(res.name, str)
    # requires core v10.10+
    core_version = res.version.number.split(".")
    assert int(core_version[0]) >= 10
    assert int(core_version[1]) > 9


def test_token_():
    res = client.login()
    assert isinstance(res, Token)
    assert res.access_token is None
    assert res.refresh_token is None


def test_v3_config_get():
    res = client.v3_config_get()
    assert isinstance(res, ConfigSaved)
    assert res.config.api.auth.enable is False


jwt_config = {
    "api": {"auth": {"enable": True, "username": "admin", "password": "test"}},
    "srt": {"enable": True},
    "rtmp": {"enable": True},
    "sessions": {"ip_ignorelist": []},
    "version": 3,
}


def test_v3_config_put_jwt():
    res = client.v3_config_put(config=jwt_config)
    assert isinstance(res, str)
    assert res == "OK"


def test_v3_config_reload_jwt():
    res = client.v3_config_reload()
    time.sleep(5)
    assert isinstance(res, str)
    assert res.strip().strip('"') == "OK"
