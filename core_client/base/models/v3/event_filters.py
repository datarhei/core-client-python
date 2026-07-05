from pydantic import BaseModel

from . import LogEventFilter


class EventFilters(BaseModel):
    """
    {
        "filters": [LogEventFilter]
    }
    """

    filters: list[LogEventFilter] | None = None
