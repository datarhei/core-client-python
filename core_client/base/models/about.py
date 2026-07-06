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


class AboutResources(BaseModel):
    cpu_core: float | None = None
    cpu_limit: float | None = None
    cpu_used: float | None = None
    ncpu: float | None = None
    is_throttling: bool | None = None
    memory_core_bytes: int | None = None
    memory_limit_bytes: int | None = None
    memory_total_bytes: int | None = None
    memory_used_bytes: int | None = None
    gpu: list | None = None


class About(BaseModel):
    app: str
    auths: list[str] | None = None
    created_at: datetime | None = None
    id: str | None = None
    name: str | None = None
    uptime_seconds: int | None = None
    version: AboutVersion
    resources: AboutResources | None = None
