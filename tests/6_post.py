import os
import time

import pytest

from core_client import Client
from core_client.base.models import Token
from core_client.base.models.v3 import ConfigSaved

pytestmark = pytest.mark.integration

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(base_url=f"{core_url}", username="admin", password="test", timeout=20.0)


def test_token():
    res = client.login()
    assert isinstance(res, Token)
    assert isinstance(res.access_token, str)
    assert isinstance(res.refresh_token, str)


def test_v3_config_get():
    res = client.v3_config_get()
    assert isinstance(res, ConfigSaved)
    assert res.config.api.auth.enable is True


none_jwt_config = {
    "api": {"auth": {"enable": False, "username": "", "password": ""}},
    "srt": {"enable": False},
    "rtmp": {"enable": False},
    "sessions": {"ip_ignorelist": []},
    "version": 3,
}


def test_v3_config_put():
    res = client.v3_config_put(config=none_jwt_config)
    assert isinstance(res, str)
    assert res == "OK"


def test_v3_config_reload():
    res = client.v3_config_reload()
    time.sleep(5)
    assert isinstance(res, str)
    assert res.strip().strip('"') == "OK"


def test_v3_config_get_verify():
    res = client.v3_config_get()
    assert isinstance(res, ConfigSaved)
    assert res.config.api.auth.enable is False
