from pydantic import BaseModel

from . import ConfigStorageS3Auth


class ConfigStorageS3(BaseModel):
    """
    {
        "access_key_id": "string",
        "auth": ConfigStorageS3Auth,
        "bucket": "string",
        "endpoint": "string",
        "mountpoint": "string",
        "name": "string",
        "region": "string",
        "secret_access_key": "string",
        "use_ssl": true
    }
    """

    access_key_id: str
    auth: ConfigStorageS3Auth
    bucket: str
    endpoint: str
    mountpoint: str
    name: str
    region: str
    secret_access_key: str
    use_ssl: bool = True
