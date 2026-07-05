from typing import Any

from pydantic import BaseModel


class GraphResponse(BaseModel):
    """
    {
        "data": {},
        "errors": []
    }
    """

    data: Any = None
    errors: list | None = None
