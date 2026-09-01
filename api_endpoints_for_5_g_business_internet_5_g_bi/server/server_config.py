from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate
from .environment import Environment


class OauthServerProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/ts/v1"


class OauthServerProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class OauthServerStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/ts/v1"


class OauthServerStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class OauthServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: OauthServerProductionConfig = Field(default_factory=OauthServerProductionConfig)
    staging: OauthServerStagingConfig = Field(default_factory=OauthServerStagingConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.production if environment == "production" else self.staging
        return UrlTemplate(base_url=variant.base_url, path=path)


class OauthServerConfigDict(TypedDict):
    production: NotRequired[OauthServerProductionConfigDict]
    staging: NotRequired[OauthServerStagingConfigDict]


class ThingspaceProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api"


class ThingspaceProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class ThingspaceStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api"


class ThingspaceStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class ThingspaceConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ThingspaceProductionConfig = Field(default_factory=ThingspaceProductionConfig)
    staging: ThingspaceStagingConfig = Field(default_factory=ThingspaceStagingConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.production if environment == "production" else self.staging
        return UrlTemplate(base_url=variant.base_url, path=path)


class ThingspaceConfigDict(TypedDict):
    production: NotRequired[ThingspaceProductionConfigDict]
    staging: NotRequired[ThingspaceStagingConfigDict]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    o_auth_server: OauthServerConfig = Field(default_factory=OauthServerConfig)
    thingspace: ThingspaceConfig = Field(default_factory=ThingspaceConfig)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    o_auth_server: NotRequired[OauthServerConfigDict]
    thingspace: NotRequired[ThingspaceConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
