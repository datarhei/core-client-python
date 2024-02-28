from pydantic import BaseModel
from typing import Optional

from . import SessionCollectorActive, SessionCollectorSummary


class SessionCollector(BaseModel):
    """
    {
        "active": SessionCollectorActive,
        "summary": SessionCollectorSummary
    }
    """

    active: SessionCollectorActive
    summary: Optional[SessionCollectorSummary] = None
