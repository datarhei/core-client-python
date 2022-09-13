import os
import time

from core_client import Client
from core_client.base.models import About, Token
from core_client.base.models.v3 import ConfigSaved

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(base_url=f"{core_url}", username="", password="", timeout=10.0)


def test_ping():
    res = client.ping()
    assert type(res) is str
    assert res == "pong"


def test_about():
    res = client.about()
    assert type(res) is About
    assert type(res.name) is str


def test_token_():
    res = client.login()
    assert type(res) is Token
    assert res.access_token is None
    assert res.refresh_token is None


def test_v3_config_get():
    res = client.v3_config_get()
    assert type(res) is ConfigSaved
    assert res.config.api.auth.enable is False


jwt_config = {
    "api": {"auth": {"enable": True, "username": "admin", "password": "test"}},
    "srt": {"enable": True},
    "rtmp": {"enable": True},
    "sessions": {"ip_ignorelist": []},
}


def test_v3_config_put_jwt():
    res = client.v3_config_put(config=jwt_config)
    assert type(res) is str
    assert res == "OK"


def test_v3_config_reload_jwt():
    res = client.v3_config_reload()
    time.sleep(5)
    assert type(res) is str
    assert res == "OK"
