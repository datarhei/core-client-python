from pydantic import BaseModel
from typing import Optional


class ConfigTls(BaseModel):
    """
    {
        "address": ":8181",
        "enable": False,
        "auto": False,
        "cert_file": "",
        "key_file": ""
    }
    """

    address: Optional[str]
    enable: Optional[bool]
    auto: Optional[bool]
    cert_file: Optional[str]
    key_file: Optional[str]
