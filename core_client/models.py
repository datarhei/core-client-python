from typing import Any

from pydantic import BaseModel


class Client(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    base_url: str
    headers: dict[str, str]
    retries: int
    timeout: float
    # Optional pooled httpx.Client / httpx.AsyncClient reused across requests.
    http_client: Any = None
