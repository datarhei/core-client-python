from pydantic import BaseModel, RootModel

from . import IamUser


class IamUserList(BaseModel):
    """
    [IamUser]
    """

    RootModel: IamUser
