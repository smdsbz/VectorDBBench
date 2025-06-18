from enum import IntEnum
from pydantic import BaseModel, SecretStr

from ..api import DBConfig


class ESVersionEnum(IntEnum):
    eight = 8
    latest = 9

class AliyunElasticsearchConfig(DBConfig, BaseModel):
    #: Protocol in use to connect to the node
    scheme: str = "http"
    host: str = ""
    port: int = 9200
    user: str = "elastic"
    password: SecretStr
    es_version: ESVersionEnum = ESVersionEnum.eight

    def to_dict(self) -> dict:
        return {
            "hosts": [{"scheme": self.scheme, "host": self.host, "port": self.port}],
            "basic_auth": (self.user, self.password.get_secret_value()),
            "es_version": self.es_version.value,
        }
