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

    created_at: Optional[str]
    version: Optional[int]
    id: Optional[str]
    name: Optional[str]
    address: Optional[str]
    log: Optional[ConfigLog]
    db: Optional[ConfigDb]
    host: Optional[ConfigHost]
    api: Optional[ConfigApi]
    tls: Optional[ConfigTls]
    rtmp: Optional[ConfigRtmp]
    srt: Optional[ConfigSrt]
    storage: Optional[ConfigStorage]
    ffmpeg: Optional[ConfigFfmpeg]
    playout: Optional[ConfigPlayout]
    resources: Optional[ConfigResources]
    debug: Optional[ConfigDebug]
    metrics: Optional[ConfigMetrics]
    sessions: Optional[ConfigSessions]
    service: Optional[ConfigService]
    router: Optional[ConfigRouter]
    cluster: Optional[ConfigCluster]
