from pydantic import BaseModel
from typing import Optional


class RtmpConnection(BaseModel):
    """
    api.RTMPConnection - a publisher or subscriber of an RTMP channel
    (GET /api/v3/rtmp/channels).

    {
        "created_at": 0,
        "remote": "string",
        "rx_bytes": 0,
        "tx_bytes": 0
    }
    """

    created_at: int | None = None
    remote: str | None = None
    rx_bytes: int | None = None
    tx_bytes: int | None = None
