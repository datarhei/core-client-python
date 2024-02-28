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

    enable: Optional[bool] = None
    ip_ignorelist: Optional[List[str]] = None
    max_bitrate_mbit: Optional[float] = None
    max_sessions: Optional[int] = None
    persist: Optional[bool] = None
    persist_interval_sec: Optional[int] = None
    session_timeout_sec: Optional[int] = None
    session_log_buffer_sec: Optional[int] = None
    session_log_path_pattern: Optional[str] = None
    session_timeout_sec: Optional[int] = None
