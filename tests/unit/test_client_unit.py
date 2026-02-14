import jwt

import core_client
from core_client import Client


def test_expected_methods_are_exposed():
    client = Client(base_url="http://example.com")

    assert hasattr(client, "v3_cluster_node_put_state")
    assert hasattr(client, "v3_process_get_report")
    assert hasattr(client, "v3_iam_put_user_policy_list")


def test_basic_login_uses_resolved_domain_in_url(monkeypatch):
    access = jwt.encode({"exp": 4102444800}, "secret", algorithm="HS256")
    refresh = jwt.encode({"exp": 4102444800}, "secret", algorithm="HS256")
    seen = {}

    class Response:
        status_code = 200

        @staticmethod
        def json():
            return {"access_token": access, "refresh_token": refresh}

    def fake_post(**kwargs):
        seen["url"] = kwargs["url"]
        return Response()

    monkeypatch.setattr(core_client.httpx, "post", fake_post)

    client = Client(
        base_url="http://example.com",
        username="admin",
        password="secret",
        domain="tenant-a",
    )
    token = client._basic_login()

    assert seen["url"] == "http://example.com/api/login?domain=tenant-a"
    assert token.access_token == access
    assert token.refresh_token == refresh


def test_token_can_be_read_before_login():
    token = Client(base_url="http://example.com").token()

    assert token.access_token is None
    assert token.refresh_token is None
    assert token.expires_at is None


def test_invalid_refresh_token_does_not_raise_decode_error(monkeypatch):
    seen = {"about_calls": 0}

    class Response:
        status_code = 200

        @staticmethod
        def json():
            return {"app": "core", "version": {"number": "16.0.0"}, "auths": None}

    def fake_get(**kwargs):
        seen["about_calls"] += 1
        assert kwargs["url"] == "http://example.com/api"
        return Response()

    monkeypatch.setattr(core_client.httpx, "get", fake_get)

    client = Client(base_url="http://example.com", refresh_token="not-a-jwt")
    headers = client._get_headers()

    assert seen["about_calls"] == 1
    assert headers == {
        "accept": "application/json",
        "content-type": "application/json",
    }
