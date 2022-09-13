from pydantic import BaseModel
from typing import List, Optional

from . import SessionCollectorActiveSession


class SessionActive(BaseModel):
    """
    {
        "ffmpeg": [SessionCollectorActiveSession],
        "hls": [SessionCollectorActiveSession],
        "hlsingress": [SessionCollectorActiveSession],
        "http": [SessionCollectorActiveSession],
        "rtmp": [SessionCollectorActiveSession],
        "srt": [SessionCollectorActiveSession]
    }
    """

    ffmpeg: Optional[List[SessionCollectorActiveSession]]
    hls: Optional[List[SessionCollectorActiveSession]]
    hlsingress: Optional[List[SessionCollectorActiveSession]]
    http: Optional[List[SessionCollectorActiveSession]]
    rtmp: Optional[List[SessionCollectorActiveSession]]
    srt: Optional[List[SessionCollectorActiveSession]]
