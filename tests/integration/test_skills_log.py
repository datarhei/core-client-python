import pytest

from core_client.base.models.v3 import Log, Skills

pytestmark = pytest.mark.integration


def test_skills_get(admin_client):
    assert isinstance(admin_client.v3_skills_get(), Skills)


def test_skills_reload(admin_client):
    assert isinstance(admin_client.v3_skills_reload(), Skills)


@pytest.mark.parametrize("fmt", [None, "console", "raw"], ids=["default", "console", "raw"])
def test_log_get(admin_client, fmt):
    res = admin_client.v3_log_get() if fmt is None else admin_client.v3_log_get(format=fmt)
    assert isinstance(res, Log)
