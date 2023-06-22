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

    address: Optional[str]
    enable: Optional[bool]
    auto: Optional[bool]
    cert_file: Optional[str]
    key_file: Optional[str]
    email: Optional[str]
