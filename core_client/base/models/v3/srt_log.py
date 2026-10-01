from pydantic import BaseModel
from typing import List, Optional


class SrtLog(BaseModel):
    """
    api.SRTLog - one entry of the `log` map of an SRT channel or connection.

    {
        "ts": 0,
        "msg": ["string"]
    }
    """

    ts: int | None = None
    msg: list[str] | None = None
