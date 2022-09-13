from pydantic import BaseModel


class SessionCollectorSummary(BaseModel):
    """
    {
        "remote": {},
        "local": {},
        "reference": {},
        "sessions": 0,
        "traffic_rx_mb": 0,
        "traffic_tx_mb": 0
    }
    """

    remote: dict
    local: dict
    reference: dict
    sessions: int
    traffic_rx_mb: float
    traffic_tx_mb: float
