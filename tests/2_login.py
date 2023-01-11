import os
import pytest
import httpx
import datetime

from core_client import Client

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")

fake_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleGkiOjYwMCwiZXhwIjoxNjczNDM3NDg5LCJpYXQiOjE2NzM0MzY4ODksImlzcyI6ImRhdGFyaGVpLWNvcmUiLCJqdGkiOiIyOGQ5N2E4Yi0yMDgxLTQ2Y2YtYjBkYy1mNGVkYWI0ZTFhYmQiLCJzdWIiOiJhZG1pbiIsInVzZWZvciI6ImFjY2VzcyJ9.hNTuILDgR2_3gloMAILOIJcWk28biZ9Q5ZCN3Gk8aK4"


def test_basic():
    client = Client(
        base_url=f"{core_url}", username="abc", password="abc", timeout=20.0
    )
    with pytest.raises(httpx.HTTPError) as exc_info:
        client.login()
    assert str(exc_info.value) == "Authorization failed"


def test_access_token():
    client = Client(
        base_url=f"{core_url}", access_token=fake_token, timeout=20.0
    )
    client.login()
    res = client.about_get()
    assert res.created_at is None
    client = Client(
        base_url=f"{core_url}", username="admin", password="test", timeout=20.0
    )
    token = client.login()
    client = Client(
        base_url=f"{core_url}", access_token=token.access_token, timeout=20.0
    )
    client.login()
    res = client.about_get()
    assert type(res.created_at) is datetime.datetime


def test_refresh_token():
    client = Client(
        base_url=f"{core_url}", refresh_token=fake_token, timeout=20.0
    )
    with pytest.raises(httpx.HTTPError) as exc_info:
        client.login()
    assert str(exc_info.value) == "Authorization failed"
    client = Client(
        base_url=f"{core_url}", username="admin", password="test", timeout=20.0
    )
    token = client.login()
    client = Client(
        base_url=f"{core_url}", refresh_token=token.refresh_token, timeout=20.0
    )
    client.login()
    res = client.about_get()
    assert type(res.created_at) is datetime.datetime
