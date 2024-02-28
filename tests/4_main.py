import os
import time

from core_client import Client
from core_client.base.models import Token
from core_client.base.models.v3 import (
    FilesystemFileList,
    Log,
    Metrics,
    MetricsCollection,
    Process,
    ProcessConfig,
    ProcessList,
    ProcessProbe,
    ProcessReport,
    ProcessReportHistory,
    ProcessState,
    ReportProcessList,
    Rtmp,
    RtmpList,
    Session,
    SessionActive,
    Skills,
    Srt,
    Widget,
)

core_url = os.getenv("CORE_URL", "http://127.0.0.1:8080")
client = Client(
    base_url=f"{core_url}", username="admin", password="test", timeout=20.0
)

proc_stream = {
    "id": "test",
    "reference": "test",
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
}

proc_viewer = {
    "id": "test_viewer",
    "reference": "test",
    "input": [
        {"address": "{memfs}/test.m3u8", "id": "input_0", "options": ["-re"]}
    ],
    "options": ["-err_detect", "ignore_err", "-y"],
    "output": [
        {
            "address": "-",
            "id": "output_0",
            "options": ["-c", "copy", "-f", "null"],
        }
    ],
}


def test_prepare():
    res = client.login()
    assert type(res) is Token
    assert type(res.access_token) is str
    assert type(res.refresh_token) is str


def test_v3_fs_get_file_list():
    res = client.v3_fs_get_file_list(storage="mem")
    assert type(res) is FilesystemFileList


def test_v3_fs_put_file():
    res = client.v3_fs_put_file(storage="mem", path="test.txt", data=b"test")
    assert type(res) is str


def test_v3_fs_get_file():
    res = client.v3_fs_get_file(storage="mem", path="test.txt")
    assert type(res) is bytes


def test_v3_fs_delete_file():
    res = client.v3_fs_delete_file(storage="mem", path="test.txt")
    assert type(res) is str


def test_v3_skills_get():
    res = client.v3_skills_get()
    assert type(res) is Skills


def test_v3_skills_reload():
    res = client.v3_skills_reload()
    assert type(res) is Skills


def test_v3_log_get():
    res_1 = client.v3_log_get()
    res_2 = client.v3_log_get(format="console")
    res_3 = client.v3_log_get(format="raw")
    assert type(res_1) is Log
    assert type(res_2) is Log
    assert type(res_3) is Log


def test_v3_metadata_put():
    res_1 = client.v3_metadata_put(key="1", data='"1"')
    res_2 = client.v3_metadata_put(key="2", data=1)
    res_3 = client.v3_metadata_put(key="3", data=[1])
    res_4 = client.v3_metadata_put(key="4", data={"1": 1})
    assert type(res_1) is str
    assert type(res_2) is int
    assert type(res_3) is list
    assert type(res_4) is dict


def test_v3_metadata_get():
    res_1 = client.v3_metadata_get(key="1")
    res_2 = client.v3_metadata_get(key="2")
    res_3 = client.v3_metadata_get(key="3")
    res_4 = client.v3_metadata_get(key="4")
    assert type(res_1) is str
    assert type(res_2) is int
    assert type(res_3) is list
    assert type(res_4) is dict


def test_v3_metrics_get():
    res = client.v3_metrics_get()
    res_about = client.about()
    core_version = res_about.version.number.split(".")
    if int(core_version[0]) >= 16 and int(core_version[1]) >= 10:
        assert type(res) is list
        assert type(res[0]) is MetricsCollection


def test_v3_metrics_post():
    res = client.v3_metrics_post(
        config={
            "metrics": [{"name": "session_total"}, {"name": "session_active"}]
        }
    )
    assert type(res) is Metrics


def test_v3_process_post():
    res = client.v3_process_post(config=proc_stream)
    client.v3_process_post(config=proc_viewer)
    assert type(res) is ProcessConfig
    assert res.id == "test"


def test_v3_process_get_list():
    res = client.v3_process_get_list(id="test")
    assert type(res) is ProcessList
    assert type(res[0]) is Process
    assert res[0].id == "test"


def test_v3_process_put_metadata():
    res_1 = client.v3_process_put_metadata(id="test", key="1", data='"1"')
    res_2 = client.v3_process_put_metadata(id="test", key="2", data=1)
    res_3 = client.v3_process_put_metadata(id="test", key="3", data=[1])
    res_4 = client.v3_process_put_metadata(id="test", key="4", data={"1": 1})
    assert type(res_1) is str
    assert type(res_2) is int
    assert type(res_3) is list
    assert type(res_4) is dict


def test_v3_process_get_metadata():
    res_1 = client.v3_process_get_metadata(id="test", key="1")
    res_2 = client.v3_process_get_metadata(id="test", key="2")
    res_3 = client.v3_process_get_metadata(id="test", key="3")
    res_4 = client.v3_process_get_metadata(id="test", key="4")
    assert type(res_1) is str
    assert type(res_2) is int
    assert type(res_3) is list
    assert type(res_4) is dict


def test_v3_process_get():
    res_1 = client.v3_process_get(id="test")
    res_2 = client.v3_process_get(id="test", filter="all")
    assert type(res_1) is Process
    assert type(res_1.config) is ProcessConfig
    assert type(res_1.state) is ProcessState
    assert type(res_1.report) is ProcessReport
    assert type(res_1.metadata) is dict
    assert res_2.config is None
    assert res_2.state is None
    assert res_2.report is None
    assert res_2.metadata is None


def test_v3_widget_get_process():
    time.sleep(5)
    res = client.v3_widget_get_process(id="test")
    assert type(res) is Widget
    assert res.uptime > 0


def test_v3_session_get():
    res = client.v3_session_get(
        collectors="ffmpeg,hls,hlsingress,http,rtmp,srt"
    )
    assert type(res) is Session


def test_v3_session_get_active():
    res = client.v3_session_get_active(
        collectors="ffmpeg,hls,hlsingress,http,rtmp,srt"
    )
    assert type(res) is SessionActive


def test_v3_rtmp_get():
    while True:
        res = client.v3_rtmp_get()
        if len(res) > 0:
            break
        time.sleep(1)
    assert type(res) is RtmpList
    assert type(res[0]) is Rtmp


def test_v3_srt_get():
    res = client.v3_srt_get()
    assert type(res) is Srt


def test_v3_process_put():
    res = client.v3_process_put(id="test", config=proc_stream)
    assert type(res) is ProcessConfig
    assert res.id == "test"


def test_v3_process_put_command_stop():
    res = client.v3_process_put_command(id="test", command="stop")
    assert type(res) is str
    assert res == "OK"


def test_v3_process_put_command_start():
    res = client.v3_process_put_command(id="test", command="start")
    assert res == "OK"


def test_v3_process_get_report_list():
    res = client.v3_process_get_report_list(id="test")
    assert type(res) is ProcessReport


def test_v3_process_get_report():
    report_list = client.v3_process_get_report_list(id="test")
    last_report = report_list.history[0].exited_at
    res = client.v3_process_get_report(id="test", exited_at=last_report)
    assert type(res) is ProcessReportHistory


def test_v3_report_get_process():
    res = client.v3_report_get_process(idpattern="test")
    assert type(res) is ReportProcessList


def test_v3_process_get_probe():
    res = client.v3_process_get_probe(id="test")
    assert type(res) is ProcessProbe


def test_v3_process_get_config():
    res = client.v3_process_get_config(id="test")
    assert type(res) is ProcessConfig


def test_v3_process_get_state():
    res = client.v3_process_get_state(id="test")
    assert type(res) is ProcessState


def test_v3_fs_operation_copy():
    res = client.v3_fs_put(
        source="mem://test.m3u8", target="disk://test.m3u8", operation="copy"
    )
    assert type(res) is str
    assert res == "OK"


def test_v3_fs_operation_move():
    res = client.v3_fs_put(
        source="mem://test.m3u8", target="disk://test.m3u8", operation="move"
    )
    assert type(res) is str
    assert res == "OK"


def test_v3_process_delete():
    res = client.v3_process_delete(id="test")
    assert type(res) is str
    assert res == "OK"
