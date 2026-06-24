import pytest

from core_client.base.models.v3 import Rtmp, Session, SessionActive, Srt, Widget

from .conftest import wait_until

pytestmark = pytest.mark.integration

COLLECTORS = "ffmpeg,hls,hlsingress,http,rtmp,srt"


def test_widget_get_process(admin_client, streaming_process):
    res = wait_until(
        lambda: admin_client.v3_widget_get_process(id=streaming_process),
        timeout=20.0,
    )
    assert isinstance(res, Widget)
    assert wait_until(lambda: admin_client.v3_widget_get_process(id=streaming_process).uptime > 0)


def test_session_get(admin_client, streaming_process):
    assert isinstance(admin_client.v3_session_get(collectors=COLLECTORS), Session)


def test_session_get_active(admin_client, streaming_process):
    assert isinstance(admin_client.v3_session_get_active(collectors=COLLECTORS), SessionActive)


def test_rtmp_get(admin_client, streaming_process):
    res = wait_until(lambda: admin_client.v3_rtmp_get() or None)
    res = res if res is not None else admin_client.v3_rtmp_get()
    assert isinstance(res, list)
    if res:
        assert isinstance(res[0], Rtmp)


def test_srt_get(admin_client, streaming_process):
    res = admin_client.v3_srt_get()
    assert isinstance(res, list)
    if res:
        assert isinstance(res[0], Srt)
