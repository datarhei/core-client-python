from pydantic import BaseModel


class ProcessEventFilter(BaseModel):
    """Filter for the process event streams (``/api/v3/cluster/events/process``).

    Fields mirror the process-event envelope (``type``, ``domain``, ``pid``,
    ``core_id``). ``type`` and ``domain`` are confirmed to filter server-side
    (e.g. ``type="progress"``); all fields are optional.

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
