from pydantic import BaseModel
from typing import Optional, List


class ConfigSessions(BaseModel):
    """
    {
        "enable": True,
        "ip_ignorelist": ["127.0.0.1/32", "::1/128"],
        "session_timeout_sec": 30,
        "persist": False,
        "persist_interval_sec": 300,
        "max_bitrate_mbit": 0,
        "max_sessions": 0
    }
    """

    """
    + {
        "session_log_buffer_sec": 0,
        "session_log_path_pattern": "string",
        "session_timeout_sec": 0
    }
    """

    enable: Optional[bool]
    ip_ignorelist: Optional[List[str]]
    max_bitrate_mbit: Optional[float]
    max_sessions: Optional[int]
    persist: Optional[bool]
    persist_interval_sec: Optional[int]
    session_timeout_sec: Optional[int]
    session_log_buffer_sec: Optional[int]
    session_log_path_pattern: Optional[str]
    session_timeout_sec: Optional[int]
