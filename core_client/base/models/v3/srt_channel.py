from pydantic import BaseModel
from typing import List, Optional

from . import SrtChannelConnection


class SrtChannel(BaseModel):
    """
    api.SRTChannelX - the detailed channel listing of GET /api/v3/srt/channels.
    Core marks this endpoint as EXPERIMENTAL; it may change.

    {
        "is_proxy": false,
        "name": "string",
        "publisher": SrtChannelConnection,
        "subscriber": [SrtChannelConnection]
    }
    """

    is_proxy: bool | None = None
    name: str | None = None
    publisher: SrtChannelConnection | None = None
    subscriber: list[SrtChannelConnection] | None = None
