"""Regression tests for model fixes found by auditing the models against
core-openapi.json: the `*List` root-model misuse and two field-type mismatches.
"""

import importlib

import pytest
from pydantic import RootModel

from core_client.base.models.v3 import ProcessStateProgressIOTee, Srt

LIST_MODELS = {
    "iam_user_policy_list": "IamUserPolicyList",
    "cluster_db_lock_list": "ClusterDbLockList",
    "process_list": "ProcessList",
    "config_storage_s3_list": "ConfigStorageS3List",
    "filesystem_file_list": "FilesystemFileList",
    "iam_user_list": "IamUserList",
    "cluster_node_list": "ClusterNodeList",
    "rtmp_list": "RtmpList",
    "filesystem_list": "FilesystemList",
    "report_process_list": "ReportProcessList",
}


@pytest.mark.parametrize("module,cls", LIST_MODELS.items(), ids=list(LIST_MODELS.values()))
def test_list_models_are_root_lists(module, cls):
    # Previously modeled as `class X(BaseModel): RootModel: Y`, which serialized
    # as {"RootModel": ...}; must be a RootModel over a list instead.
    model = getattr(importlib.import_module(f"core_client.base.models.v3.{module}"), cls)
    assert issubclass(model, RootModel)
    assert model.model_validate([]).model_dump() == []


def test_iam_user_policy_list_serializes_as_array():
    from core_client.base.models.v3.iam_user_policy_list import IamUserPolicyList

    dumped = IamUserPolicyList.model_validate([{"name": "p", "actions": ["GET"]}]).model_dump()
    assert isinstance(dumped, list)
    assert dumped[0]["name"] == "p"


def test_srt_socketid_is_int():
    # openapi api.SRTChannel.socketid is an integer.
    assert Srt.model_fields["socketid"].annotation == (int | None)
    srt = Srt.model_validate(
        {"name": "s", "socketid": 347916646, "subscriber": [], "connections": {}, "log": {}}
    )
    assert srt.socketid == 347916646


def test_session_token_field_is_extra_not_extras():
    from core_client.base.models.v3 import SessionToken

    assert "extra" in SessionToken.model_fields
    assert "extras" not in SessionToken.model_fields
    dumped = SessionToken(extra={"k": "v"}).model_dump()
    assert dumped["extra"] == {"k": "v"}


def test_config_has_update_check_and_compress():
    from core_client.base.models.v3 import Config, ConfigCompress

    cfg = Config.model_validate({"update_check": True, "compress": {"min_length": 100}})
    assert cfg.update_check is True
    assert isinstance(cfg.compress, ConfigCompress)
    assert cfg.compress.min_length == 100


def test_filesystem_file_accepts_core_id():
    from core_client.base.models.v3 import FilesystemFile

    f = FilesystemFile.model_validate(
        {"name": "a", "size_bytes": 1, "last_modified": 0, "core_id": "node-1"}
    )
    assert f.core_id == "node-1"


def test_about_accepts_resources():
    from core_client.base.models import About

    a = About.model_validate(
        {"app": "core", "version": {"number": "16.20.0"}, "resources": {"ncpu": 4.0}}
    )
    assert a.resources.ncpu == 4.0


def test_iotee_fifo_recovery_accepts_float():
    # openapi api.ProgressIOTee.fifo_recovery_attempts_total is a number (float).
    assert ProcessStateProgressIOTee.model_fields["fifo_recovery_attempts_total"].annotation == (
        float | None
    )
    tee = ProcessStateProgressIOTee.model_validate(
        {"address": "a", "format": "hls", "fifo_recovery_attempts_total": 2.5}
    )
    assert tee.fifo_recovery_attempts_total == 2.5
