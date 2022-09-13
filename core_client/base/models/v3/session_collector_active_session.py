from pydantic import BaseModel


class SessionCollectorActiveSession(BaseModel):
    """
    {
        "id": "restreamer-ui:ingest: 5f61d80a-7aab-4df6-8027-1d4610b814ef",
        "reference": "5f61d80a-7aab-4df6-8027-1d4610b814ef",
        "created_at": 1662548810,
        "local": "unknown",
        "remote": "unknown",
        "extra": "",
        "bytes_rx": 616691712,
        "bytes_tx": 0,
        "bandwidth_rx_kbit": 1931.2,
        "bandwidth_tx_kbit": 0
    }
    """

    id: str
    reference: str
    created_at: int
    local: str
    remote: str
    extra: str
    bytes_rx: int
    bytes_tx: int
    bandwidth_rx_kbit: float
    bandwidth_tx_kbit: float
