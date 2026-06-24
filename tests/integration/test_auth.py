import datetime

import httpx
import pytest

from core_client import Client
from core_client.base.models import About, Error

from .conftest import ADMIN_PASSWORD, ADMIN_USERNAME, CLIENT_TIMEOUT

pytestmark = pytest.mark.integration

# A syntactically valid but expired/foreign JWT.
FAKE_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleGkiOjYwMCwiZXhwIjoxNjczNDM3NDg5LCJpYXQiOjE2NzM0MzY4ODksImlzcyI6ImRhdGFyaGVpLWNvcmUiLCJqdGkiOiIyOGQ5N2E4Yi0yMDgxLTQ2Y2YtYjBkYy1mNGVkYWI0ZTFhYmQiLCJzdWIiOiJhZG1pbiIsInVzZWZvciI6ImFjY2VzcyJ9.hNTuILDgR2_3gloMAILOIJcWk28biZ9Q5ZCN3Gk8aK4"


def test_basic_login_with_wrong_credentials_fails(core_url):
    client = Client(base_url=core_url, username="abc", password="abc", timeout=CLIENT_TIMEOUT)
    with pytest.raises(httpx.HTTPError) as exc_info:
        client.login()
    assert str(exc_info.value) == "Authorization failed"


def test_access_token_injection(core_url):
    # A bogus access token still lets the client be constructed and queried.
    client = Client(base_url=core_url, access_token=FAKE_TOKEN, timeout=CLIENT_TIMEOUT)
    client.login()
    assert isinstance(client.about_get(), (Error, About))

    # A real access token obtained via basic auth works end to end.
    token = Client(
        base_url=core_url, username=ADMIN_USERNAME, password=ADMIN_PASSWORD, timeout=CLIENT_TIMEOUT
    ).login()
    client = Client(base_url=core_url, access_token=token.access_token, timeout=CLIENT_TIMEOUT)
    client.login()
    assert isinstance(client.about_get().created_at, datetime.datetime)


def test_refresh_token_injection(core_url):
    client = Client(base_url=core_url, refresh_token=FAKE_TOKEN, timeout=CLIENT_TIMEOUT)
    with pytest.raises(httpx.HTTPError) as exc_info:
        client.login()
    assert str(exc_info.value) == "Authorization failed"

    token = Client(
        base_url=core_url, username=ADMIN_USERNAME, password=ADMIN_PASSWORD, timeout=CLIENT_TIMEOUT
    ).login()
    client = Client(base_url=core_url, refresh_token=token.refresh_token, timeout=CLIENT_TIMEOUT)
    client.login()
    assert isinstance(client.about_get().created_at, datetime.datetime)
