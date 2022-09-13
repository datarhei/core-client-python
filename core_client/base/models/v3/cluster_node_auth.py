from pydantic import BaseModel, HttpUrl


class ClusterNodeAuth(BaseModel):
    address: HttpUrl
    username: str
    password: str
