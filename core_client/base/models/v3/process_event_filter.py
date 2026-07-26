from pydantic import BaseModel


class ProcessEventFilter(BaseModel):
    """Filter for the process event streams (``/api/v3/cluster/events/process``).

    The four fields match the Core ``api.ProcessEventFilter`` struct exactly. Each
    value is a **case-insensitive, unanchored regular expression** matched against
    the corresponding event field; omitted fields are ignored, and all provided
    fields must match (AND). For example ``type="progress"`` selects progress
    events, ``pid="abc"`` matches any process id containing ``abc``, and
    ``type="progress|report"`` matches either type.

    ``extra="forbid"`` keeps the ``EventFilters`` union unambiguous — a dict with a
    ``type`` key resolves to this model rather than ``LogEventFilter``.

    {
        "type": "progress",
        "domain": "string",
        "pid": "string",
        "core_id": "string"
    }
    """

    model_config = {"extra": "forbid"}

    type: str | None = None
    domain: str | None = None
    pid: str | None = None
    core_id: str | None = None
