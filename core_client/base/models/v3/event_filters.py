from pydantic import BaseModel

from . import LogEventFilter, ProcessEventFilter


class EventFilters(BaseModel):
    """
    {
        "filters": [LogEventFilter | ProcessEventFilter]
    }

    Log-event streams (``/api/v3/events``, ``/api/v3/cluster/events``) use
    ``LogEventFilter``; process-event streams (``/api/v3/cluster/events/process``)
    use ``ProcessEventFilter`` (filter by ``type``, ``domain``, ...). Raw ``dict``
    filters are also accepted by the endpoints for backwards compatibility.
    """

    filters: list[LogEventFilter | ProcessEventFilter] | None = None
