from pydantic import BaseModel
from typing import Optional

from . import ProcessProgress


class ProcessEvent(BaseModel):
    """
    An event from the process event streams (POST /api/v3/events/process and
    POST /api/v3/cluster/events/process). Pass it as `model=` to the streaming
    methods for typed events.

    {
        "core_id": "string",
        "domain": "string",
        "line": "string",
        "pid": "string",
        "progress": ProcessProgress,
        "ts": 0,
        "type": "string"
    }
    """

    core_id: str | None = None
    domain: str | None = None
    line: str | None = None
    pid: str | None = None
    progress: ProcessProgress | None = None
    ts: int | None = None
    type: str | None = None
