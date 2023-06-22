from pydantic import BaseModel


class IamUserAuthApiAuth0Tenant(BaseModel):
    """
    {
        "audience": "string",
        "client_id": "string",
        "domain": "string"
    }
    """

    audience: str
    client_id: str
    domain: str
