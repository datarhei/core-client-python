from pydantic import BaseModel, RootModel

from . import IamUserPolicy


class IamUserPolicyList(BaseModel):
    """
    [IamUserPolicy]
    """

    RootModel: IamUserPolicy
