"""Shared fixtures and helpers for the integration test suite.

These tests run against a live datarhei Core instance (``CORE_URL``) and are
only collected when ``RUN_INTEGRATION_TESTS`` is truthy (see ``tests/conftest.py``).

The fixtures here remove the boilerplate that used to be copy-pasted into every
test module and decouple the individual test files from each other:

* ``manage_auth`` (autouse, session) brackets the whole run by enabling JWT auth
  before the tests and restoring the original (disabled) state afterwards. This
  is the only place that owns the global auth lifecycle.
* ``admin_client`` / ``anon_client`` provide ready-to-use clients.
* ``streaming_process`` provides a long-lived, running process for read-only
  tests, while ``process_factory`` hands out isolated, auto-cleaned processes
  for tests that mutate process state.

As a result every test module is self-contained and can be run on its own.
"""

import os
import time

import pytest

from core_client import Client

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "test"
CLIENT_TIMEOUT = 20.0

# JWT auth enabled (also enables srt/rtmp so the streaming process can publish).
AUTH_ENABLED_CONFIG = {
    "api": {"auth": {"enable": True, "username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}},
    "srt": {"enable": True},
    "rtmp": {"enable": True},
    "sessions": {"ip_ignorelist": []},
    "version": 3,
}

# JWT auth disabled, restoring the pristine state of a fresh Core.
AUTH_DISABLED_CONFIG = {
    "api": {"auth": {"enable": False, "username": "", "password": ""}},
    "srt": {"enable": False},
    "rtmp": {"enable": False},
    "sessions": {"ip_ignorelist": []},
    "version": 3,
}

PROC_STREAM = {
    "id": "test",
    "reference": "test",
    "owner": "testuser",
    "input": [
        {
            "address": "testsrc2=rate=25:size=16x9",
            "id": "input_0",
            "options": ["-re", "-f", "lavfi"],
        }
    ],
    "options": ["-err_detect", "ignore_err", "-y"],
    "output": [
        {
            "address": "[f=hls:start_number=0:hls_time=2:hls_list_size=6:hls_flags=append_list+delete_segments:hls_segment_filename={memfs^:}/{processid}_%04d.ts:method=PUT]{memfs}/{processid}.m3u8|[f=flv]{rtmp,name=test.stream}|[f=mpegts]{srt,name=test,mode=publish}",
            "cleanup": [
                {"pattern": "memfs:/{processid}_*.ts", "purge_on_delete": True},
                {"pattern": "memfs:/{processid}.m3u8", "purge_on_delete": True},
            ],
            "id": "output_0",
            "options": [
                "-map", "0:v",
                "-codec:v", "libx264",
                "-r", "25",
                "-flags", "+global_header",
                "-tag:v", "7",
                "-tag:a", "10",
                "-f", "tee",
            ],
        }
    ],
}

PROC_VIEWER = {
    "id": "test_viewer",
    "reference": "test",
    "owner": "testuser",
    "input": [{"address": "{memfs}/test.m3u8", "id": "input_0", "options": ["-re"]}],
    "options": ["-err_detect", "ignore_err", "-y"],
    "output": [
        {
            "address": "-",
            "id": "output_0",
            "options": ["-c", "copy", "-f", "null"],
        }
    ],
}


def wait_until(predicate, *, timeout=30.0, interval=0.5):
    """Poll ``predicate`` until it returns a truthy value or ``timeout`` elapses.

    Returns the last value produced by ``predicate`` (truthy on success, falsy
    on timeout), so callers can both wait and assert on the result. Exceptions
    raised by ``predicate`` are treated as "not ready yet"; this is essential
    while the Core restarts its HTTP server during a config reload and briefly
    drops connections.
    """
    deadline = time.monotonic() + timeout

    def _poll():
        try:
            return predicate()
        except Exception:
            return False

    result = _poll()
    while not result and time.monotonic() < deadline:
        time.sleep(interval)
        result = _poll()
    return result


def _auth_enabled(client):
    """Return the ``api.auth.enable`` flag, or ``None`` if it cannot be read."""
    config = client.v3_config_get()
    try:
        return config.config.api.auth.enable
    except AttributeError:
        return None


def _process_running(client, process_id):
    process = client.v3_process_get(id=process_id)
    state = getattr(process, "state", None)
    return getattr(state, "exec", None) == "running"


@pytest.fixture(scope="session")
def core_url():
    return os.getenv("CORE_URL", "http://127.0.0.1:8080")


def _new_client(core_url, *, admin=False):
    if admin:
        return Client(
            base_url=core_url,
            username=ADMIN_USERNAME,
            password=ADMIN_PASSWORD,
            timeout=CLIENT_TIMEOUT,
        )
    return Client(base_url=core_url, username="", password="", timeout=CLIENT_TIMEOUT)


@pytest.fixture(scope="session", autouse=True)
def manage_auth(core_url):
    """Enable JWT auth for the whole session and restore the original state.

    Owns the global auth lifecycle so individual test modules never have to.
    Assumes a fresh Core with auth disabled (the documented test precondition).
    """
    anon = _new_client(core_url)
    admin = _new_client(core_url, admin=True)

    assert anon.v3_config_put(config=AUTH_ENABLED_CONFIG) == "OK"
    anon.v3_config_reload()

    def _ready():
        try:
            admin.login()
        except Exception:
            return False
        return _auth_enabled(admin) is True

    assert wait_until(_ready), "JWT auth was not enabled in time"

    yield

    admin.login()
    assert admin.v3_config_put(config=AUTH_DISABLED_CONFIG) == "OK"
    admin.v3_config_reload()
    wait_until(lambda: _auth_enabled(_new_client(core_url)) is False)


@pytest.fixture
def anon_client(core_url, manage_auth):
    """Client without credentials; auth is enabled so protected calls fail."""
    return _new_client(core_url)


@pytest.fixture(scope="module")
def admin_client(core_url, manage_auth):
    client = _new_client(core_url, admin=True)
    client.login()
    return client


@pytest.fixture
def process_factory(admin_client):
    """Create isolated processes that are deleted automatically after the test.

    Call it to POST a process (defaults to a copy of ``PROC_STREAM`` with a
    unique id) and optionally wait until it is running. Returns the
    ``v3_process_post`` result.
    """
    created = []
    counter = {"n": 0}

    def _create(config=None, *, wait_running=False):
        cfg = dict(config) if config else dict(PROC_STREAM)
        if config is None:
            counter["n"] += 1
            cfg["id"] = f"test_factory_{counter['n']}"
        result = admin_client.v3_process_post(config=cfg)
        created.append(cfg["id"])
        if wait_running:
            wait_until(lambda: _process_running(admin_client, cfg["id"]))
        return result

    yield _create

    for process_id in reversed(created):
        admin_client.v3_process_delete(id=process_id)


@pytest.fixture(scope="module")
def streaming_process(admin_client):
    """A long-lived running process (id ``test``) plus its HLS viewer.

    Read-only tests depend on this without owning its lifecycle. Both processes
    are removed when the module finishes.
    """
    admin_client.v3_process_post(config=PROC_STREAM)
    admin_client.v3_process_post(config=PROC_VIEWER)
    wait_until(lambda: _process_running(admin_client, PROC_STREAM["id"]))

    yield PROC_STREAM["id"]

    admin_client.v3_process_delete(id=PROC_VIEWER["id"])
    admin_client.v3_process_delete(id=PROC_STREAM["id"])
