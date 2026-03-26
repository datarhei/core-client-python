from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, Union


class AboutVersion(BaseModel):
    number: str
    repository_commit: str | None = None
    repository_branch: str | None = None
    build_date: datetime | str | None = None
    arch: str | None = None
    compiler: str | None = None


class About(BaseModel):
    app: str
    auths: list[str] | None = None
    created_at: datetime | None = None
    id: str | None = None
    name: str | None = None
    uptime_seconds: int | None = None
    version: AboutVersion
