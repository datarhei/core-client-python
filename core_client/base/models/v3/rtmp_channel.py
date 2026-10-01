from pydantic import BaseModel
from typing import List, Optional

from . import RtmpConnection


class RtmpChannel(BaseModel):
    """
    api.RTMPChannel - the detailed channel listing of GET /api/v3/rtmp/channels.
    GET /api/v3/rtmp returns the name-only form instead (see Rtmp).

    {
        "is_proxy": false,
        "name": "string",
        "publisher": RtmpConnection,
        "subscriber": [RtmpConnection]
    }
    """

    is_proxy: bool | None = None
    name: str | None = None
    publisher: RtmpConnection | None = None
    subscriber: list[RtmpConnection] | None = None
