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

    address: Optional[str] = None
    enable: Optional[bool] = None
    auto: Optional[bool] = None
    cert_file: Optional[str] = None
    key_file: Optional[str] = None
    email: Optional[str] = None
