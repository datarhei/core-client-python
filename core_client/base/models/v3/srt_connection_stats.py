from pydantic import BaseModel, model_validator
from typing import Optional


class SrtConnectionStats(BaseModel):
    """
    v16.11.0

    -sent_unique__bytes
    +sent_unique_bytes
    -recv_loss__bytes
    +recv_loss_bytes
    """

    """
    {
        "timestamp_ms": 2325052658,
        "sent_pkt": 0,
        "recv_pkt": 598424409,
        "sent_unique_pkt": 0,
        "recv_unique_pkt": 598424402,
        "send_loss_pkt": 0,
        "recv_loss_pkt": 9,
        "sent_retrans_pkt": 0,
        "recv_retran_pkts": 7,
        "sent_ack_pkt": 147773635,
        "recv_ack_pkt": 0,
        "sent_nak_pkt": 2,
        "recv_nak_pkt": 0,
        "send_km_pkt": 0,
        "recv_km_pkt": 0,
        "send_duration_us": 0,
        "send_drop_pkt": 0,
        "recv_drop_pkt": 7,
        "recv_undecrypt_pkt": 0,
        "sent_bytes": 0,
        "recv_bytes": 680449226780,
        "sent_unique_bytes": 0,
        "recv_unique_bytes": 680449217120,
        "recv_loss_bytes": 9295,
        "sent_retrans_bytes": 0,
        "send_drop_bytes": 0,
        "recv_drop_bytes": 9660,
        "recv_undecrypt_bytes": 0,
        "pkt_send_period_us": 0,
        "flow_window_pkt": 0,
        "flight_size_pkt": 0,
        "rtt_ms": 0,
        "bandwidth_mbit": 0,
        "avail_send_buf_bytes": 0,
        "avail_recv_buf_bytes": 0,
        "max_bandwidth_mbit": 0,
        "mss_bytes": 0,
        "send_buf_pkt": 0,
        "send_buf_bytes": 0,
        "send_buf_ms": 0,
        "send_tsbpd_delay_ms": 0,
        "recv_buf_pkt": 0,
        "recv_buf_bytes": 0,
        "recv_buf_ms": 0,
        "recv_tsbpd_delay_ms": 0,
        "reorder_tolerance_pkt": 0,
        "pkt_recv_avg_belated_time_ms": 0
    }
    """

    timestamp_ms: int
    sent_pkt: int
    recv_pkt: int
    sent_unique_pkt: int
    recv_unique_pkt: int
    send_loss_pkt: int
    recv_loss_pkt: int
    sent_retrans_pkt: int
    recv_retran_pkts: int
    sent_ack_pkt: int
    recv_ack_pkt: int
    sent_nak_pkt: int
    recv_nak_pkt: int
    send_km_pkt: int
    recv_km_pkt: int
    send_duration_us: int
    send_drop_pkt: int
    recv_drop_pkt: int
    recv_undecrypt_pkt: int
    sent_bytes: int
    recv_bytes: int
    sent_unique__bytes: Optional[int] = None
    sent_unique_bytes: Optional[int] = None
    recv_unique_bytes: int
    recv_loss__bytes: Optional[int] = None
    recv_loss_bytes: Optional[int] = None
    sent_retrans_bytes: int
    send_drop_bytes: int
    recv_drop_bytes: int
    recv_undecrypt_bytes: int
    pkt_send_period_us: float
    flow_window_pkt: int
    flight_size_pkt: int
    rtt_ms: float
    bandwidth_mbit: float
    avail_send_buf_bytes: int
    avail_recv_buf_bytes: int
    max_bandwidth_mbit: float
    mss_bytes: int
    send_buf_pkt: int
    send_buf_bytes: int
    send_buf_ms: int
    send_tsbpd_delay_ms: int
    recv_buf_pkt: int
    recv_buf_bytes: int
    recv_buf_ms: int
    recv_tsbpd_delay_ms: int
    reorder_tolerance_pkt: int
    pkt_recv_avg_belated_time_ms: int

    @model_validator(mode="before")
    def remove_empty(cls, values):
        if values["sent_unique__bytes"] is None:
            values.pop("sent_unique__bytes")
            values.pop("recv_loss__bytes")
        else:
            values.pop("sent_unique_bytes")
            values.pop("recv_loss_bytes")
        return values
