from pydantic import BaseModel
from typing import Optional


class ConfigTls(BaseModel):
    """
    {
        "address": ":8181",
        "enable": False,
        "auto": False,
        "cert_file": "string",
        "key_file": "string"
    }
    """

    """
    + {
        "email": "string"
    }
    """

    address: str | None = None
    enable: bool | None = None
    auto: bool | None = None
    cert_file: str | None = None
    key_file: str | None = None
    email: str | None = None
