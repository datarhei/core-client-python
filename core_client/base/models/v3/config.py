from pydantic import BaseModel
from typing import Optional

from . import (
    ConfigApi,
    ConfigCluster,
    ConfigCompress,
    ConfigDb,
    ConfigDebug,
    ConfigFfmpeg,
    ConfigHost,
    ConfigLog,
    ConfigMetrics,
    ConfigPlayout,
    ConfigResources,
    ConfigRouter,
    ConfigRtmp,
    ConfigService,
    ConfigSessions,
    ConfigSrt,
    ConfigStorage,
    ConfigTls,
)


class Config(BaseModel):
    """
    # v2, v3
    {
        "created_at": "2022-09-07T19:18:06.320318744Z",
        "version": 2,
        "id": "b6be32da-d322-40fd-9c89-7b7444b9b2a5",
        "name": "dark-salad-0799",
        "address": ":8080",
        "update_check": True,
        "log": ConfigLog,
        "db": ConfigDb,
        "host": ConfigHost,
        "api": ConfigApi,
        "tls": ConfigTls,
        "storage": ConfigStorage,
        "rtmp": ConfigRtmp,
        "srt": ConfigSrt,
        "ffmpeg": ConfigFfmpeg,
        "playout": ConfigPlayout,
        "debug": ConfigDebug,
        "metrics": ConfigMetrics,
        "sessions": ConfigSessions,
        "service": ConfigService,
        "router": ConfigRouter
    }
    """

    """
    + {
        "resources": ConfigResources,
        "cluster": ConfigCluster
    }
    """

    created_at: str | None = None
    version: int | None = None
    id: str | None = None
    name: str | None = None
    address: str | None = None
    update_check: bool | None = None
    compress: ConfigCompress | None = None
    log: ConfigLog | None = None
    db: ConfigDb | None = None
    host: ConfigHost | None = None
    api: ConfigApi | None = None
    tls: ConfigTls | None = None
    rtmp: ConfigRtmp | None = None
    srt: ConfigSrt | None = None
    storage: ConfigStorage | None = None
    ffmpeg: ConfigFfmpeg | None = None
    playout: ConfigPlayout | None = None
    resources: ConfigResources | None = None
    debug: ConfigDebug | None = None
    metrics: ConfigMetrics | None = None
    sessions: ConfigSessions | None = None
    service: ConfigService | None = None
    router: ConfigRouter | None = None
    cluster: ConfigCluster | None = None
