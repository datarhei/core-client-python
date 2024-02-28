from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, Union


class AboutVersion(BaseModel):
    number: str
    repository_commit: Optional[str] = None
    repository_branch: Optional[str] = None
    build_date: Optional[Union[datetime, str]] = None
    arch: Optional[str] = None
    compiler: Optional[str] = None


class About(BaseModel):
    app: str
    auths: Optional[List[str]] = None
    created_at: Optional[datetime] = None
    id: Optional[str] = None
    name: Optional[str] = None
    uptime_seconds: Optional[int] = None
    version: AboutVersion
