"""Regression tests for the endpoints and model fields added after diffing the
client against the current Core OpenAPI doc (96 paths / 125 definitions).

Most of these are cluster or newer-Core routes that cannot be exercised against a
standalone Core, so request construction is asserted without a backend.
"""

import pytest

from core_client import AsyncClient, Client
from core_client.base.api import (
    v3_cluster_process_get_config,
    v3_cluster_process_get_report,
    v3_cluster_process_get_state,
    v3_rtmp_get_channels,
    v3_rtmp_put_disconnect,
    v3_srt_get_channels,
    v3_srt_put_disconnect,
)
from core_client.models import Client as ClientModel


def _minimal(model, **overrides):
    """Payload with every required field of `model` set to 0, plus overrides.

    Several of these models (SrtConnectionStats, ClusterNodeResources) predate
    the all-optional convention and still have required fields.
    """
    data = {name: 0 for name, f in model.model_fields.items() if f.is_required()}
    data.update(overrides)
    return data


@pytest.fixture
def cm():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


NEW_METHODS = [
    "v3_cluster_process_get_config",
    "v3_cluster_process_get_state",
    "v3_cluster_process_get_report",
    "v3_rtmp_get_channels",
    "v3_rtmp_put_disconnect",
    "v3_srt_get_channels",
    "v3_srt_put_disconnect",
]

NEW_STREAM_METHODS = ["v3_events_process_stream", "v3_events_log_stream"]


def test_new_methods_registered():
    client = Client(base_url="http://example.com")
    for name in NEW_METHODS:
        assert hasattr(client, name), name


def test_new_stream_methods_are_async_only():
    for name in NEW_STREAM_METHODS:
        assert hasattr(AsyncClient, name), name
        assert not hasattr(Client, name), name


def test_request_construction(cm):
    cases = [
        (v3_cluster_process_get_config._build_request(cm, id="p1", domain="d"), "get",
         "http://h/api/v3/cluster/process/p1/config?domain=d"),
        (v3_cluster_process_get_state._build_request(cm, id="p1", domain="d"), "get",
         "http://h/api/v3/cluster/process/p1/state?domain=d"),
        (v3_cluster_process_get_report._build_request(cm, id="p1", created_at=1, exited_at=2), "get",
         "http://h/api/v3/cluster/process/p1/report?domain=&created_at=1&exited_at=2"),
        (v3_rtmp_get_channels._build_request(cm), "get", "http://h/api/v3/rtmp/channels"),
        (v3_rtmp_put_disconnect._build_request(cm, path="*"), "put",
         "http://h/api/v3/rtmp/disconnect?path=*"),
        (v3_srt_get_channels._build_request(cm), "get", "http://h/api/v3/srt/channels"),
        (v3_srt_put_disconnect._build_request(cm), "put", "http://h/api/v3/srt/disconnect"),
    ]
    for (request, _), method, url in cases:
        assert request["method"] == method, (request["method"], url)
        assert request["url"] == url


def test_stream_request_urls(cm):
    from core_client.base.api import v3_events_log_stream, v3_events_process_stream

    assert v3_events_process_stream._build_request(cm)[:2] == (
        "POST", "http://h/api/v3/events/process")
    # /events/log is Core's alias of /events (same LogEvents handler).
    assert v3_events_log_stream._build_request(cm)[:2] == ("POST", "http://h/api/v3/events/log")


# --- models ------------------------------------------------------------------


def test_rtmp_channel_model():
    from core_client.base.models.v3 import RtmpChannel

    ch = RtmpChannel.model_validate({
        "name": "/live/stream",
        "is_proxy": False,
        "publisher": {"created_at": 1788466169, "remote": "1.2.3.4:5", "rx_bytes": 10, "tx_bytes": 0},
        "subscriber": [{"created_at": 1788466170, "remote": "1.2.3.5:6", "rx_bytes": 0, "tx_bytes": 99}],
    })
    assert ch.publisher.rx_bytes == 10
    assert ch.subscriber[0].tx_bytes == 99


def test_srt_channel_model_carries_stats():
    from core_client.base.models.v3 import SrtChannel, SrtConnectionStats

    ch = SrtChannel.model_validate({
        "name": "/live/stream",
        "is_proxy": True,
        "publisher": {
            "created_at": 1788466169,
            "remote": "1.2.3.4:5",
            "rx_bytes": 1,
            "tx_bytes": 2,
            "stats": _minimal(SrtConnectionStats, bandwidth_mbit=12.5),
        },
        "subscriber": [],
    })
    assert ch.is_proxy is True
    assert ch.publisher.stats.bandwidth_mbit == 12.5


def test_process_event_model():
    from core_client.base.models.v3 import ProcessEvent

    ev = ProcessEvent.model_validate({
        "pid": "p1", "domain": "d", "core_id": "c1", "ts": 1788469276, "type": "progress",
        "progress": {
            "speed": 1.0, "time": 42.5,
            "input": [{"id": "i0", "fps": 25.0, "bitrate": 2400.0, "iomap": [0, 1],
                       "avstream": {"enabled": True, "drop": 0, "dup": 0, "looping": False}}],
            "output": [{"id": "o0", "fps": 25.0, "q": 12.5, "iomap": [0]}],
        },
    })
    assert ev.progress.input[0].avstream.enabled is True
    assert ev.progress.input[0].iomap == [0, 1]
    assert ev.progress.output[0].q == 12.5


def test_srt_log_is_a_list_of_entries():
    # Core sends map[string][]SRTLog; this used to be typed dict[str, str] and
    # raised a ValidationError as soon as the log was non-empty.
    from core_client.base.models.v3 import Srt, SrtConnection, SrtConnectionStats

    payload = {"SRT.cn": [{"ts": 1788469276, "msg": ["connection established"]}]}
    srt = Srt.model_validate(
        {"name": "ch", "socketid": 1, "subscriber": [2], "connections": {}, "log": payload}
    )
    assert srt.log["SRT.cn"][0].msg == ["connection established"]
    assert srt.log["SRT.cn"][0].ts == 1788469276

    conn = SrtConnection.model_validate(
        {"log": payload, "stats": _minimal(SrtConnectionStats)}
    )
    assert conn.log["SRT.cn"][0].msg == ["connection established"]


def test_gpu_resources_are_typed():
    from core_client.base.models import AboutResources
    from core_client.base.models.v3 import ClusterNodeResources

    gpu = {"memory_total_bytes": 8 * 1024**3, "usage_encoder": 12.5, "usage_general": 7.0}
    assert AboutResources.model_validate({"gpu": [gpu]}).gpu[0].usage_encoder == 12.5
    resources = ClusterNodeResources.model_validate(_minimal(ClusterNodeResources, gpu=[gpu]))
    assert resources.gpu[0].memory_total_bytes == 8 * 1024**3


def test_progress_io_and_avstream_fields():
    from core_client.base.models.v3 import ProcessStateProgressIOAvstream, ProcessStateProgressIO

    assert "iomap" in ProcessStateProgressIO.model_fields
    for field in ("channels", "codec", "height", "layout", "level",
                  "pix_fmt", "profile", "sample_fmt", "sampling_hz", "width"):
        assert field in ProcessStateProgressIOAvstream.model_fields, field


def test_mapping_map_has_id():
    from core_client.base.models.v3 import ProcessStateProgressMappingMap

    m = ProcessStateProgressMappingMap.model_validate(
        {"id": "g0", "input": 1, "output": -1, "index": 0, "name": "graph_0_in_1_0", "copy": False}
    )
    assert m.id == "g0"
    assert m.copy is False
