from pydantic import BaseModel
from typing import Optional


class ProcessProgressInputAvstream(BaseModel):
    """
    api.ProcessProgressInputAVstream - the avstream part of an input in a
    process event's progress payload (POST /api/v3/events/process).

    {
        "drop": 0,
        "dup": 0,
        "enabled": true,
        "enc": 0,
        "looping": false,
        "time": 0
    }
    """

    drop: int | None = None
    dup: int | None = None
    enabled: bool | None = None
    enc: int | None = None
    looping: bool | None = None
    time: int | None = None
