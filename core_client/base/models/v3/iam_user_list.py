from pydantic import RootModel

from . import IamUser

# JSON array of IamUser.
IamUserList = RootModel[list[IamUser]]
