from pydantic import BaseModel
from typing import Optional

from . import (
    ConfigApi,
    ConfigCluster,
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

    created_at: Optional[str] = None
    version: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    log: Optional[ConfigLog] = None
    db: Optional[ConfigDb] = None
    host: Optional[ConfigHost] = None
    api: Optional[ConfigApi] = None
    tls: Optional[ConfigTls] = None
    rtmp: Optional[ConfigRtmp] = None
    srt: Optional[ConfigSrt] = None
    storage: Optional[ConfigStorage] = None
    ffmpeg: Optional[ConfigFfmpeg] = None
    playout: Optional[ConfigPlayout] = None
    resources: Optional[ConfigResources] = None
    debug: Optional[ConfigDebug] = None
    metrics: Optional[ConfigMetrics] = None
    sessions: Optional[ConfigSessions] = None
    service: Optional[ConfigService] = None
    router: Optional[ConfigRouter] = None
    cluster: Optional[ConfigCluster] = None
