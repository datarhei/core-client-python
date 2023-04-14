from typing import List, Optional

from pydantic import BaseModel

from . import ProcessStateExec, ProcessStateProgress


class ProcessReportHistory(BaseModel):
    """
    {
        "created_at": "2022-07-28T13:10:03+00:00",
        "log": [
            [ "1659013803", "ffmpeg version 4.4.1-datarhei Copyright (c) 2000-2021 the FFmpeg developers" ],
            [ "1659013803", "  built with gcc 10.3.1 (Alpine 10.3.1_git20211027) 20211027" ],
        ],
        "prelude": [
            "ffmpeg version 4.4.1-datarhei Copyright (c) 2000-2021 the FFmpeg developers",
            "  built with gcc 10.3.1 (Alpine 10.3.1_git20211027) 20211027",
        ]
    }
    """

    """new in vod branch
    {
        "exited_at": int,
        "exit_state": ProcessStateExec,
        "progress": ProcessStateProgress
        "matches": [str]
    }
    """

    created_at: int
    prelude: Optional[List[str]] = []
    log: Optional[List[List[str]]] = []
    matches: Optional[List[str]] = []
    exited_at: Optional[int]
    exit_state: Optional[ProcessStateExec]
    progress: Optional[ProcessStateProgress]
