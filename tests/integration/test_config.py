import pytest

from core_client import Client
from core_client.base.models import Token
from core_client.base.models.v3 import ConfigSaved

from .conftest import (
    AUTH_DISABLED_CONFIG,
    AUTH_ENABLED_CONFIG,
    CLIENT_TIMEOUT,
    _auth_enabled,
    wait_until,
)

pytestmark = pytest.mark.integration


def test_config_get_reports_auth_enabled(admin_client):
    res = admin_client.v3_config_get()
    assert isinstance(res, ConfigSaved)
    assert res.config.api.auth.enable is True


def test_config_put_reload_roundtrip(admin_client, core_url):
    """Disable auth, verify, then re-enable so the session invariant holds.

    Covers the config put/reload endpoints and both auth states. The test is
    self-restoring: it always leaves JWT auth enabled, which the session-level
    ``manage_auth`` fixture expects.
    """
    anon = Client(base_url=core_url, username="", password="", timeout=CLIENT_TIMEOUT)

    # Disable auth.
    assert admin_client.v3_config_put(config=AUTH_DISABLED_CONFIG) == "OK"
    assert admin_client.v3_config_reload().strip().strip('"') == "OK"
    assert wait_until(lambda: _auth_enabled(anon) is False), "auth was not disabled"

    # With auth off, an anonymous login yields an empty token.
    token = anon.login()
    assert isinstance(token, Token)
    assert token.access_token is None
    assert token.refresh_token is None

    # Re-enable auth (anonymous client suffices while auth is off).
    assert anon.v3_config_put(config=AUTH_ENABLED_CONFIG) == "OK"
    assert anon.v3_config_reload().strip().strip('"') == "OK"

    admin = Client(
        base_url=core_url, username="admin", password="test", timeout=CLIENT_TIMEOUT
    )
    assert wait_until(lambda: (admin.login(), _auth_enabled(admin))[1] is True), "auth was not re-enabled"
