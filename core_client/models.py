from pydantic import BaseModel
from typing import Dict


class Client(BaseModel):
    base_url: str
    headers: dict[str, str]
    retries: int
    timeout: float
