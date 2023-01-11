from pydantic import BaseModel


class ConfigApiAuthAuth0Tenant(BaseModel):
    """
    {
        "audience": "string",
        "clientid": "string",
        "domain": "string",
        "users": [
            "string"
        ]
    }
    """

    audience: str
    clientid: str
    domain: str
    users: list[str]
