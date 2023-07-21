from typing import List, Optional

from . import ProcessReportHistory


class ProcessReport(ProcessReportHistory):
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
        ],
        "history": [ProcessReportHistory]
    }
    """

    """
    v16.13.0
    {
        "matches": "[freezedetect @ 0x7fa240e1da00] lavfi.freezedetect.freeze_start: 106.480.997x"
    }
    """

    history: Optional[List[ProcessReportHistory]]
