"""Unit tests for the event filter models and their serialization."""

from core_client.base.api import v3_cluster_post_events, v3_events_post
from core_client.base.models.v3 import EventFilters, LogEventFilter, ProcessEventFilter
from core_client.models import Client as ClientModel


def _cm():
    return ClientModel(base_url="http://h", headers={}, retries=3, timeout=10.0)


def test_log_filter_body_has_no_none_fields():
    filters = EventFilters(filters=[LogEventFilter(event="ProcessReport")])
    request, _ = v3_events_post._build_request(_cm(), filters=filters)
    assert request["json"] == {"filters": [{"event": "ProcessReport"}]}


def test_process_filter_body_has_no_none_fields():
    filters = EventFilters(filters=[ProcessEventFilter(type="progress")])
    request, _ = v3_cluster_post_events._build_request(_cm(), filters=filters)
    assert request["json"] == {"filters": [{"type": "progress"}]}


def test_union_resolves_raw_dicts():
    parsed = EventFilters(filters=[{"type": "progress"}, {"event": "X"}, {"domain": "d"}])
    assert [type(f).__name__ for f in parsed.filters] == [
        "ProcessEventFilter",
        "LogEventFilter",
        "ProcessEventFilter",
    ]


def test_raw_dict_filters_pass_through():
    # Backwards compatibility: a raw dict body is sent verbatim.
    request, _ = v3_events_post._build_request(_cm(), filters={"filters": [{"type": "progress"}]})
    assert request["json"] == {"filters": [{"type": "progress"}]}
