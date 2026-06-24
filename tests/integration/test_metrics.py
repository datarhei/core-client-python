import pytest

from core_client.base.models.v3 import Metrics, MetricsCollection

pytestmark = pytest.mark.integration


def test_metrics_get(admin_client):
    res = admin_client.v3_metrics_get()
    major, minor, *_ = admin_client.about().version.number.split(".")
    if (int(major), int(minor)) >= (16, 10):
        assert isinstance(res, list)
        if res:
            assert isinstance(res[0], MetricsCollection)


def test_metrics_post(admin_client):
    res = admin_client.v3_metrics_post(
        config={"metrics": [{"name": "session_total"}, {"name": "session_active"}]}
    )
    assert isinstance(res, Metrics)


def test_metrics_generic(admin_client):
    # v3_metrics is the generic POST helper underlying v3_metrics_post.
    res = admin_client.v3_metrics(config={"metrics": [{"name": "session_total"}]})
    assert isinstance(res, Metrics)
