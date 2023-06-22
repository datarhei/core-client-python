from pydantic import BaseModel

from . import IamUserAuthApiAuth0Tenant


class IamUserAuthApiAuth0(BaseModel):
    """
    {
        "tenant": IamUserAuthApiAuth0Tenant,
        "user": "string"
    }
    """

    tenant: IamUserAuthApiAuth0Tenant
    user: str
