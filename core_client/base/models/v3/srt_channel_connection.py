from pydantic import BaseModel
from typing import Optional

from . import SrtConnectionStats


class SrtChannelConnection(BaseModel):
    """
    api.SRTConnectionX - a publisher or subscriber of an SRT channel
    (GET /api/v3/srt/channels). Not to be confused with SrtConnection, the
    entry of the `connections` map of GET /api/v3/srt.

    {
        "created_at": 0,
        "remote": "string",
        "rx_bytes": 0,
        "stats": SrtConnectionStats,
        "tx_bytes": 0
    }
    """

    created_at: int | None = None
    remote: str | None = None
    rx_bytes: int | None = None
    stats: SrtConnectionStats | None = None
    tx_bytes: int | None = None
