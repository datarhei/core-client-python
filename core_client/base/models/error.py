from pydantic import BaseModel
from typing import Any, List


class Error(BaseModel):
    code: int
    message: str
    details: list[Any]
