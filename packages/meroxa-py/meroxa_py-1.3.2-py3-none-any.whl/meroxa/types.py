from enum import Enum
from typing import Any


class ResourceType(Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"
    REDSHIFT = "redshift"
    URL = "url"
    S3 = "s3"
    MONGODB = "mongodb"
    ELASTICSEARCH = "elasticsearch"
    SNOWFLAKE = "snowflakedb"
    BIGQUERY = "bigquery"
    SQLSERVER = "sqlserver"
    COSMODB = "cosmodb"
    KAFKA = "kafka"
    CONFLUENTCLOUD = "confluentcloud"


class MeroxaApiResponse(object):
    def __init__(self, *args, **kwargs):
        ...


class EnvironmentIdentifier:
    def __init__(self, name=None, uuid=None):
        self.name = name
        self.uuid = uuid

    def repr_json(self):
        return dict(name=self.name) if self.name is not None else dict(uuid=self.uuid)


class ResourceCollection:
    def __init__(self, name=None, destination=None, source=None):

        self.name = name
        self.source = source
        self.destination = destination


class ApplicationResource:
    def __init__(self, name=None, uuid=None, collection: Any = None):

        self.name = name
        self.uuid = uuid
        self.collection = ResourceCollection(**collection)


class EntityIdentifier:
    def __init__(self, name=None, uuid=None):
        self.name = name
        self.uuid = uuid

    def repr_json(self):
        return dict(name=self.name) if self.name is not None else dict(uuid=self.uuid)


class ResourceNode:
    def __init__(
        self,
        connectors: list[dict[str, str]] = None,
        functions: list[dict[str, str]] = None,
    ) -> None:
        self.connectors = connectors
        self.functions = functions

    def repr_json(self):
        res = {}

        if self.connectors:
            res.update(self.connectors)

        if self.functions:
            res.update(self.functions)

        return res
