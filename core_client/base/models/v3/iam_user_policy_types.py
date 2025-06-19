from enum import Enum


class IamUserPolicyTypes(str, Enum):
    """
    "type": ["fs", "srt", "rtmp, "process", "iam", "api"]
    """

    fs = "fs"
    srt = "srt"
    rtmp = "rtmp"
    process = "process"
    iam = "iam"
    api = "api"
