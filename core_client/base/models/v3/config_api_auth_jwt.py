from pydantic import BaseModel
from typing import Optional


class ConfigApiAuthJwt(BaseModel):
    """
    {
        "secret": "ch_IqztB[?d-Z.De3jWttnnOLwkCIa_G"
    }
    """

    secret: Optional[str] = None
