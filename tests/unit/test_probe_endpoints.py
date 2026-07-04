"""Unit tests for the probe-by-config endpoints and the probe stream model.

``POST /api/v3/process/probe`` (and its cluster sibling) require a recent Core
and cannot be exercised against an older/standalone instance, so request
building is covered here without a backend.
"""

import pytest

from core_client import Client
from core_client.base.api import (
    v3_cluster_process_post_probe,
    v3_process_post_probe,
)
from core_client.base.models.v3 import ProcessProbeStream
from core_client.models import Client as ClientModel

CONFIG = {"id": "x", "reference": "r", "options": [], "input": [], "output": []}


@pytest.fixture
def client_model():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


def test_process_post_probe_is_registered():
    assert hasattr(Client(base_url="http://example.com"), "v3_process_post_probe")


def test_process_post_probe_request(client_model):
    request, _ = v3_process_post_probe._build_request(client_model, config=CONFIG)
    assert request["method"] == "post"
    assert request["url"] == "http://h/api/v3/process/probe"
    # config is validated into a ProcessConfig and serialized back to a dict
    assert request["json"]["id"] == "x"
    assert request["json"]["reference"] == "r"


def test_cluster_process_post_probe_coreid(client_model):
    request, _ = v3_cluster_process_post_probe._build_request(
        client_model, config=CONFIG, coreid="node-1"
    )
    assert request["method"] == "post"
    assert request["url"] == "http://h/api/v3/cluster/process/probe?coreid=node-1"


def test_probe_stream_accepts_fractional_numbers():
    # fps / bitrate_kbps / duration_sec are floats per the Core API.
    stream = ProcessProbeStream.model_validate(
        {
            "bitrate_kbps": 128.5,
            "channels": 2,
            "codec": "h264",
            "coder": "h264",
            "duration_sec": 57261.914,
            "format": "hls",
            "fps": 29.97,
            "height": 720,
            "index": 0,
            "language": "und",
            "layout": "",
            "pix_fmt": "yuv420p",
            "sampling_hz": 0,
            "stream": 0,
            "type": "video",
            "url": "u",
            "width": 1280,
        }
    )
    assert stream.fps == 29.97
    assert stream.bitrate_kbps == 128.5
    assert stream.duration_sec == 57261.914
