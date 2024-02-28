from enum import Enum


class IamUserPolicyTypes(str, Enum):
    """
    "type": ["fs", "srt", "rtmp"]
    """

    fs = "fs"
    srt = "srt"
    rtmp = "rtmp"
    process = "process"
