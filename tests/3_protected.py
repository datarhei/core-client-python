import os

from core_client import Client
from core_client.base.models import About, Error

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(base_url=f"{core_url}", username="", password="", timeout=20.0)


def test_about():
    res = client.about()
    assert type(res) is About
    assert res.name is None


def test_v3_config_get():
    res = client.v3_config_get()
    assert type(res) is Error


def test_v3_process_get_list():
    res = client.v3_process_get_list()
    assert type(res) is Error


def test_v3_rtmp_get():
    res = client.v3_rtmp_get()
    assert type(res) is Error


def test_v3_srt_get():
    res = client.v3_srt_get()
    assert type(res) is Error


def test_v3_fs_get_list():
    res = client.v3_fs_get_list()
    assert type(res) is Error


def test_v3_skills_get():
    res = client.v3_skills_get()
    assert type(res) is Error


def test_v3_log_get():
    res = client.v3_log_get()
    assert type(res) is Error
