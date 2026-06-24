import pytest

from core_client.base.models import Error
from core_client.base.models.v3 import (
    Process,
    ProcessConfig,
    ProcessProbe,
    ProcessReport,
    ProcessState,
    ReportProcess,
)

from .conftest import PROC_STREAM

pytestmark = pytest.mark.integration


# --- lifecycle (isolated processes via process_factory) ---------------------


def test_process_post(process_factory):
    res = process_factory()
    assert isinstance(res, ProcessConfig)


def test_process_put(admin_client, process_factory):
    proc = process_factory()
    updated = dict(PROC_STREAM, id=proc.id)
    res = admin_client.v3_process_put(id=proc.id, config=updated)
    assert isinstance(res, ProcessConfig)
    assert res.id == proc.id


def test_process_command_stop_start(admin_client, process_factory):
    proc = process_factory(wait_running=True)
    assert admin_client.v3_process_put_command(id=proc.id, command="stop") == "OK"
    assert admin_client.v3_process_put_command(id=proc.id, command="start") == "OK"


def test_process_delete(admin_client, process_factory):
    proc = process_factory()
    res = admin_client.v3_process_delete(id=proc.id)
    assert res == "OK"


def test_process_metadata_roundtrip(admin_client, process_factory):
    proc = process_factory()
    cases = [("1", '"1"', str), ("2", 1, int), ("3", [1], list), ("4", {"1": 1}, dict)]
    for key, value, expected in cases:
        assert isinstance(admin_client.v3_process_put_metadata(id=proc.id, key=key, data=value), expected)
        assert isinstance(admin_client.v3_process_get_metadata(id=proc.id, key=key), expected)


# --- read-only views (shared running streaming_process) ---------------------


def test_process_get_list(admin_client, streaming_process):
    res = admin_client.v3_process_get_list(id=streaming_process)
    assert isinstance(res, list)
    assert res[0].id == streaming_process
    assert isinstance(res[0], Process)


def test_process_get_full_vs_filtered(admin_client, streaming_process):
    # Ensure the process has metadata so the full view exposes it as a dict.
    admin_client.v3_process_put_metadata(id=streaming_process, key="probe", data='"set"')

    full = admin_client.v3_process_get(id=streaming_process)
    assert isinstance(full, Process)
    assert isinstance(full.config, ProcessConfig)
    assert isinstance(full.state, ProcessState)
    assert isinstance(full.report, ProcessReport)
    assert isinstance(full.metadata, dict)

    filtered = admin_client.v3_process_get(id=streaming_process, filter="all")
    assert filtered.config is None
    assert filtered.state is None
    assert filtered.report is None
    assert filtered.metadata is None


def test_process_get_config(admin_client, streaming_process):
    assert isinstance(admin_client.v3_process_get_config(id=streaming_process), ProcessConfig)


def test_process_get_state(admin_client, streaming_process):
    assert isinstance(admin_client.v3_process_get_state(id=streaming_process), ProcessState)


def test_process_get_probe(admin_client, streaming_process):
    assert isinstance(admin_client.v3_process_get_probe(id=streaming_process), ProcessProbe)


def test_process_get_report_list(admin_client, streaming_process):
    assert isinstance(admin_client.v3_process_get_report_list(id=streaming_process), ProcessReport)


def test_process_get_report_list_filtered(admin_client, streaming_process):
    report = admin_client.v3_process_get_report_list(id=streaming_process, domain="")
    assert isinstance(report, ProcessReport)
    if not report.history:
        pytest.skip("No report history available yet")
    exited_at = report.history[0].exited_at
    if exited_at is None:
        pytest.skip("No exited_at value available yet")
    res = admin_client.v3_process_get_report_list(id=streaming_process, exited_at=exited_at)
    assert isinstance(res, ProcessReport)


def test_report_get_process(admin_client, streaming_process):
    res = admin_client.v3_report_get_process(idpattern=streaming_process)
    assert isinstance(res, (list, Error))
    if isinstance(res, list) and res:
        assert isinstance(res[0], ReportProcess)


def test_process_get_report_alias(admin_client, streaming_process):
    # v3_process_get_report is the documented alias of v3_report_get_process.
    res = admin_client.v3_process_get_report(idpattern=streaming_process)
    assert isinstance(res, (list, Error))
