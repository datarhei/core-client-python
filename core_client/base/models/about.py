from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, Union


class AboutVersion(BaseModel):
    number: str
    repository_commit: Optional[str]
    repository_branch: Optional[str]
    build_date: Optional[Union[datetime, str]]
    arch: Optional[str]
    compiler: Optional[str]


class About(BaseModel):
    app: str
    auths: Optional[List[str]]
    created_at: Optional[datetime]
    id: Optional[str]
    name: Optional[str]
    uptime_seconds: Optional[int]
    version: AboutVersion
