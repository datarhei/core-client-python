from pydantic import BaseModel
from typing import Optional


class SessionCollectorActiveSessionHlsSegments(BaseModel):
    """
    {
        "requests": 1447,
        "failed": 0,
        "too_slow": 0,
        "retries": 3,
        "too_late": 0,
        "sequence_gaps": 17,
        "last": 1788469276
    }
    """

    requests: int | None = None
    failed: int | None = None
    too_slow: int | None = None
    retries: int | None = None
    too_late: int | None = None
    sequence_gaps: int | None = None
    last: int | None = None
