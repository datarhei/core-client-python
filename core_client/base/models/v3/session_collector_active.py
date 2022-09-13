from pydantic import BaseModel
from typing import List

from . import SessionCollectorActiveSession


class SessionCollectorActive(BaseModel):
    """
    {
        "list": [SessionCollectorActiveSession],
        "sessions": 1,
        "bandwidth_rx_mbit": 1.977,
        "bandwidth_tx_mbit": 0,
        "max_sessions": 0,
        "max_bandwidth_rx_mbit": 0,
        "max_bandwidth_tx_mbit": 0
    }
    """

    list: List[SessionCollectorActiveSession]
    sessions: int
    bandwidth_rx_mbit: float
    bandwidth_tx_mbit: float
    max_sessions: int
    max_bandwidth_rx_mbit: float
    max_bandwidth_tx_mbit: float
