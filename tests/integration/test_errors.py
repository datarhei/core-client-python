import pytest

from core_client.base.models import Error
from core_client.base.models.v3 import ProcessProbe, Session, SessionActive

from .conftest import PROC_STREAM

pytestmark = pytest.mark.integration


def test_fs_get_file_list_unknown_storage(admin_client):
    assert isinstance(admin_client.v3_fs_get_file_list(storage="unknown"), Error)


def test_fs_put_file_unknown_storage(admin_client):
    assert isinstance(admin_client.v3_fs_put_file(storage="unknown", path="x.txt", data=b"x"), Error)


def test_fs_get_file_unknown_storage(admin_client):
    assert isinstance(admin_client.v3_fs_get_file(storage="unknown", path="x.txt"), Error)


def test_fs_get_file_missing_path(admin_client):
    assert isinstance(admin_client.v3_fs_get_file(storage="mem", path="does-not-exist.txt"), Error)


def test_fs_delete_file_unknown_storage(admin_client):
    assert isinstance(admin_client.v3_fs_delete_file(storage="unknown", path="x.txt"), Error)


def test_metadata_get_unknown(admin_client):
    assert isinstance(admin_client.v3_metadata_get(key="unknown"), Error)


def test_process_get_list_unknown_returns_empty(admin_client):
    res = admin_client.v3_process_get_list(id="unknown")
    assert isinstance(res, list)
    assert len(res) == 0


def test_process_get_metadata_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get_metadata(id="unknown", key="unknown"), Error)


def test_process_get_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get(id="unknown"), Error)


def test_widget_get_process_unknown(admin_client):
    assert isinstance(admin_client.v3_widget_get_process(id="unknown"), Error)


def test_process_put_unknown(admin_client):
    assert isinstance(admin_client.v3_process_put(id="unknown", config=PROC_STREAM), Error)


def test_process_get_report_list_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get_report_list(id="unknown"), Error)


def test_report_get_process_unknown(admin_client):
    assert isinstance(admin_client.v3_report_get_process(idpattern="unknown"), (list, Error))


def test_process_get_probe_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get_probe(id="unknown", domain=""), (Error, ProcessProbe))


def test_process_get_config_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get_config(id="unknown"), Error)


def test_process_get_state_unknown(admin_client):
    assert isinstance(admin_client.v3_process_get_state(id="unknown"), Error)


def test_process_delete_unknown(admin_client):
    assert isinstance(admin_client.v3_process_delete(id="unknown"), Error)


def test_process_put_command_unknown(admin_client):
    assert isinstance(admin_client.v3_process_put_command(id="unknown", command="start"), Error)


@pytest.mark.parametrize("getter", ["v3_session_get", "v3_session_get_active"])
def test_session_unknown_collectors_empty(admin_client, getter):
    res = getattr(admin_client, getter)(collectors="unknown")
    assert isinstance(res, (Session, SessionActive))
    assert res.ffmpeg is None
    assert res.hls is None
    assert res.hlsingress is None
    assert res.http is None
    assert res.rtmp is None
    assert res.srt is None
