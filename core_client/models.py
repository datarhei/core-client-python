from pydantic import BaseModel
from typing import Dict


class Client(BaseModel):
    base_url: str
    headers: Dict[str, str]
    retries: int
    timeout: float
