import pytest

from core_client.base.models import Error

pytestmark = pytest.mark.integration


def test_fs_get_file_list(admin_client):
    assert isinstance(admin_client.v3_fs_get_file_list(storage="mem"), list)


def test_fs_file_put_get_delete_roundtrip(admin_client):
    assert isinstance(admin_client.v3_fs_put_file(storage="mem", path="test.txt", data=b"test"), str)
    assert admin_client.v3_fs_get_file(storage="mem", path="test.txt") == b"test"
    assert isinstance(admin_client.v3_fs_delete_file(storage="mem", path="test.txt"), str)


def test_fs_get_file_exists(admin_client):
    admin_client.v3_fs_put_file(storage="mem", path="exists.txt", data=b"x")
    res = admin_client.v3_fs_get_file_exists(storage="mem", path="exists.txt")
    assert not isinstance(res, Error)
    assert isinstance(res, bytes)
    admin_client.v3_fs_delete_file(storage="mem", path="exists.txt")


def test_fs_get_file_exists_missing(admin_client):
    # HEAD on a missing file returns a 404 with an empty body; the client must
    # surface it as an Error instead of failing to parse an empty JSON body.
    res = admin_client.v3_fs_get_file_exists(storage="mem", path="does-not-exist.txt")
    assert isinstance(res, Error)
    assert res.code == 404


@pytest.mark.parametrize("operation", ["copy", "move"])
def test_fs_operation(admin_client, streaming_process, operation):
    # Source is produced by the running streaming process; tolerate a 404 in
    # case the segment is not on disk yet.
    res = admin_client.v3_fs_put(
        source="mem://test.m3u8", target="disk://test.m3u8", operation=operation
    )
    assert isinstance(res, (str, Error))
    if isinstance(res, str):
        assert res.strip().strip('"') == "OK"
    else:
        assert res.code == 404
