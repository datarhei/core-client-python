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

    enable: bool | None = None
    ip_ignorelist: list[str] | None = None
    max_bitrate_mbit: float | None = None
    max_sessions: int | None = None
    persist: bool | None = None
    persist_interval_sec: int | None = None
    session_timeout_sec: int | None = None
    session_log_buffer_sec: int | None = None
    session_log_path_pattern: str | None = None
    session_timeout_sec: int | None = None
