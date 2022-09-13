import os
import time

from core_client import Client
from core_client.base.models import Token
from core_client.base.models.v3 import ConfigSaved

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(base_url=f"{core_url}", username="admin", password="test", timeout=10.0)


def test_token():
    res = client.login()
    assert type(res) is Token
    assert type(res.access_token) is str
    assert type(res.refresh_token) is str


def test_v3_config_get():
    res = client.v3_config_get()
    assert type(res) is ConfigSaved
    assert res.config.api.auth.enable is True


none_jwt_config = {
    "api": {"auth": {"enable": False, "username": "", "password": ""}},
    "srt": {"enable": False},
    "rtmp": {"enable": False},
    "sessions": {"ip_ignorelist": []},
}


def test_v3_config_put():
    res = client.v3_config_put(config=none_jwt_config)
    assert type(res) is str
    assert res == "OK"


def test_v3_config_reload():
    res = client.v3_config_reload()
    time.sleep(5)
    assert type(res) is str
    assert res == "OK"


def test_v3_config_get_verify():
    res = client.v3_config_get()
    assert type(res) is ConfigSaved
    assert res.config.api.auth.enable is False
