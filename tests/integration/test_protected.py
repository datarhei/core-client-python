import pytest

from core_client.base.models import About, Error

pytestmark = pytest.mark.integration


def test_about_hides_details_without_auth(anon_client):
    res = anon_client.about()
    assert isinstance(res, About)
    assert res.name is None


@pytest.mark.parametrize(
    "call",
    [
        lambda c: c.v3_config_get(),
        lambda c: c.v3_process_get_list(),
        lambda c: c.v3_rtmp_get(),
        lambda c: c.v3_srt_get(),
        lambda c: c.v3_fs_get_list(),
        lambda c: c.v3_skills_get(),
        lambda c: c.v3_log_get(),
    ],
    ids=["config", "process_list", "rtmp", "srt", "fs_list", "skills", "log"],
)
def test_protected_endpoints_require_auth(anon_client, call):
    assert isinstance(call(anon_client), Error)
