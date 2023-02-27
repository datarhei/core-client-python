import os

from core_client import Client
from core_client.base.models import Error, Token
from core_client.base.models.v3 import (
    ProcessList,
    ProcessProbe,
    Session,
    SessionActive,
)

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(
    base_url=f"{core_url}", username="admin", password="test", timeout=20.0
)

proc_stream = {
    "autostart": True,
    "id": "test",
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
                {
                    "pattern": "memfs:/{processid}_*.ts",
                    "purge_on_delete": True,
                },
                {
                    "pattern": "memfs:/{processid}.m3u8",
                    "purge_on_delete": True,
                },
            ],
            "id": "output_0",
            "options": [
                "-map",
                "0:v",
                "-codec:v",
                "libx264",
                "-r",
                "25",
                "-flags",
                "+global_header",
                "-tag:v",
                "7",
                "-tag:a",
                "10",
                "-f",
                "tee",
            ],
        }
    ],
    "reconnect": True,
    "reconnect_delay_seconds": 15,
    "reference": "test",
    "stale_timeout_seconds": 30,
    "type": "ffmpeg",
}


def test_prepare():
    res = client.login()
    assert type(res) is Token
    assert type(res.access_token) is str
    assert type(res.refresh_token) is str


def test_v3_fs_get_file_list():
    res = client.v3_fs_get_file_list(name="unknown")
    assert type(res) is Error


def test_v3_fs_put_file():
    res = client.v3_fs_put_file(name="unknown", path="test.txt", data=b"test")
    assert type(res) is Error


def test_v3_fs_get_file():
    res = client.v3_fs_get_file(name="unknown", path="test.txt")
    assert type(res) is Error


def test_v3_fs_get_file_2():
    res = client.v3_fs_get_file(name="mem", path="test.txt")
    assert type(res) is Error


def test_v3_fs_delete_file():
    res = client.v3_fs_delete_file(name="unknown", path="test.txt")
    assert type(res) is Error


def test_v3_metadata_get():
    res = client.v3_metadata_get(key="unkbown")
    assert type(res) is Error


def test_v3_process_get_list():
    res = client.v3_process_get_list(id="unknown")
    assert type(res) is ProcessList
    assert len(res) == 0


def test_v3_process_get_metadata():
    res = client.v3_process_get_metadata(id="unknown", key="unknown")
    assert type(res) is Error


def test_v3_process_get():
    res = client.v3_process_get(id="unknown")
    assert type(res) is Error


def test_v3_widget_get_process():
    res = client.v3_widget_get_process(id="unknown")
    assert type(res) is Error


def test_v3_session_get():
    res = client.v3_session_get(collectors="unknown")
    assert type(res) is Session
    assert res.ffmpeg is None
    assert res.hls is None
    assert res.hlsingress is None
    assert res.http is None
    assert res.rtmp is None
    assert res.srt is None


def test_v3_session_get_active():
    res = client.v3_session_get_active(collectors="unknown")
    assert type(res) is SessionActive
    assert res.ffmpeg is None
    assert res.hls is None
    assert res.hlsingress is None
    assert res.http is None
    assert res.rtmp is None
    assert res.srt is None


def test_v3_process_put():
    res = client.v3_process_put(id="unknown", config=proc_stream)
    assert type(res) is Error


def test_v3_process_get_report():
    res = client.v3_process_get_report(id="unknown")
    assert type(res) is Error


def test_v3_process_get_probe():
    res = client.v3_process_get_probe(id="unknown")
    assert type(res) is ProcessProbe
    assert res.log[0] == "Unknown process ID (unknown)"


def test_v3_process_get_config():
    res = client.v3_process_get_config(id="unknown")
    assert type(res) is Error


def test_v3_process_get_state():
    res = client.v3_process_get_state(id="unknown")
    assert type(res) is Error


def test_v3_process_delete():
    res = client.v3_process_delete(id="unknown")
    assert type(res) is Error


def test_v3_process_put_command_start():
    res = client.v3_process_put_command(id="unknown", command="start")
    assert type(res) is Error
