from typing import List, Optional

from pydantic import BaseModel

from . import ProcessStateExec, ProcessStateProgress, ProcessStateResources


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
    + {
        "lines": { "error": 5, "info": 48484834, "warning": 1 }
    }
    """

    created_at: int
    prelude: list[str] | None = []
    log: list[list[str]] | None = []
    lines: dict[str, int] | None = {}
    matches: list[str] | None = []
    exited_at: int | None = None
    exit_state: ProcessStateExec | None = None
    progress: ProcessStateProgress | None = None
    resources: ProcessStateResources | None = None
