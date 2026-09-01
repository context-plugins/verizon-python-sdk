from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate
from .environment import Environment


class HyperPreciseCredentialsProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/auth/v1"


class HyperPreciseCredentialsProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseCredentialsStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/auth/v1"


class HyperPreciseCredentialsStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseCredentialsDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/auth/v1"


class HyperPreciseCredentialsDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseCredentialsQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/auth/v1"


class HyperPreciseCredentialsQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseCredentialsMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/auth/v1"


class HyperPreciseCredentialsMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseCredentialsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: HyperPreciseCredentialsProductionConfig = Field(default_factory=HyperPreciseCredentialsProductionConfig)
    staging: HyperPreciseCredentialsStagingConfig = Field(default_factory=HyperPreciseCredentialsStagingConfig)
    dev: HyperPreciseCredentialsDevConfig = Field(default_factory=HyperPreciseCredentialsDevConfig)
    qa: HyperPreciseCredentialsQaConfig = Field(default_factory=HyperPreciseCredentialsQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        HyperPreciseCredentialsMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=HyperPreciseCredentialsMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class HyperPreciseCredentialsConfigDict(TypedDict):
    production: NotRequired[HyperPreciseCredentialsProductionConfigDict]
    staging: NotRequired[HyperPreciseCredentialsStagingConfigDict]
    dev: NotRequired[HyperPreciseCredentialsDevConfigDict]
    qa: NotRequired[HyperPreciseCredentialsQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        HyperPreciseCredentialsMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class ImpServerProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://imp.thingspace.verizon.com"


class ImpServerProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class ImpServerStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://imp-staging.thingspace.verizon.com"


class ImpServerStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class ImpServerDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.imp.thingspace.verizon.com"


class ImpServerDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class ImpServerQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.imp.thingspace.verizon.com"


class ImpServerQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class ImpServerMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com"


class ImpServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class ImpServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ImpServerProductionConfig = Field(default_factory=ImpServerProductionConfig)
    staging: ImpServerStagingConfig = Field(default_factory=ImpServerStagingConfig)
    dev: ImpServerDevConfig = Field(default_factory=ImpServerDevConfig)
    qa: ImpServerQaConfig = Field(default_factory=ImpServerQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        ImpServerMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=ImpServerMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class ImpServerConfigDict(TypedDict):
    production: NotRequired[ImpServerProductionConfigDict]
    staging: NotRequired[ImpServerStagingConfigDict]
    dev: NotRequired[ImpServerDevConfigDict]
    qa: NotRequired[ImpServerQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        ImpServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


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


class ThingspaceDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com/api"


class ThingspaceDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class ThingspaceQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api"


class ThingspaceQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class ThingspaceMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api"


class ThingspaceMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class ThingspaceConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ThingspaceProductionConfig = Field(default_factory=ThingspaceProductionConfig)
    staging: ThingspaceStagingConfig = Field(default_factory=ThingspaceStagingConfig)
    dev: ThingspaceDevConfig = Field(default_factory=ThingspaceDevConfig)
    qa: ThingspaceQaConfig = Field(default_factory=ThingspaceQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        ThingspaceMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=ThingspaceMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class ThingspaceConfigDict(TypedDict):
    production: NotRequired[ThingspaceProductionConfigDict]
    staging: NotRequired[ThingspaceStagingConfigDict]
    dev: NotRequired[ThingspaceDevConfigDict]
    qa: NotRequired[ThingspaceQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        ThingspaceMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


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


class OauthServerDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/ts/v1"


class OauthServerDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class OauthServerQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/ts/v1"


class OauthServerQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class OauthServerMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/ts/v1"


class OauthServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class OauthServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: OauthServerProductionConfig = Field(default_factory=OauthServerProductionConfig)
    staging: OauthServerStagingConfig = Field(default_factory=OauthServerStagingConfig)
    dev: OauthServerDevConfig = Field(default_factory=OauthServerDevConfig)
    qa: OauthServerQaConfig = Field(default_factory=OauthServerQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        OauthServerMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=OauthServerMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class OauthServerConfigDict(TypedDict):
    production: NotRequired[OauthServerProductionConfigDict]
    staging: NotRequired[OauthServerStagingConfigDict]
    dev: NotRequired[OauthServerDevConfigDict]
    qa: NotRequired[OauthServerQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        OauthServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class M2MProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/m2m"


class M2MProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class M2MStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/m2m"


class M2MStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class M2MDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/m2m"


class M2MDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class M2MQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/m2m"


class M2MQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class M2MMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/m2m"


class M2MMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class M2MConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: M2MProductionConfig = Field(default_factory=M2MProductionConfig)
    staging: M2MStagingConfig = Field(default_factory=M2MStagingConfig)
    dev: M2MDevConfig = Field(default_factory=M2MDevConfig)
    qa: M2MQaConfig = Field(default_factory=M2MQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        M2MMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=M2MMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class M2MConfigDict(TypedDict):
    production: NotRequired[M2MProductionConfigDict]
    staging: NotRequired[M2MStagingConfigDict]
    dev: NotRequired[M2MDevConfigDict]
    qa: NotRequired[M2MQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        M2MMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class DeviceLocationProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/loc/v1"


class DeviceLocationProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceLocationStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/loc/v1"


class DeviceLocationStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceLocationDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/loc/v1"


class DeviceLocationDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceLocationQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/loc/v1"


class DeviceLocationQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceLocationMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/loc/v1"


class DeviceLocationMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceLocationConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: DeviceLocationProductionConfig = Field(default_factory=DeviceLocationProductionConfig)
    staging: DeviceLocationStagingConfig = Field(default_factory=DeviceLocationStagingConfig)
    dev: DeviceLocationDevConfig = Field(default_factory=DeviceLocationDevConfig)
    qa: DeviceLocationQaConfig = Field(default_factory=DeviceLocationQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        DeviceLocationMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=DeviceLocationMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class DeviceLocationConfigDict(TypedDict):
    production: NotRequired[DeviceLocationProductionConfigDict]
    staging: NotRequired[DeviceLocationStagingConfigDict]
    dev: NotRequired[DeviceLocationDevConfigDict]
    qa: NotRequired[DeviceLocationQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        DeviceLocationMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class SubscriptionServerProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/subsc/v1"


class SubscriptionServerProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class SubscriptionServerStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/subsc/v1"


class SubscriptionServerStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class SubscriptionServerDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/subsc/v1"


class SubscriptionServerDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class SubscriptionServerQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/subsc/v1"


class SubscriptionServerQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class SubscriptionServerMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/subsc/v1"


class SubscriptionServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class SubscriptionServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: SubscriptionServerProductionConfig = Field(default_factory=SubscriptionServerProductionConfig)
    staging: SubscriptionServerStagingConfig = Field(default_factory=SubscriptionServerStagingConfig)
    dev: SubscriptionServerDevConfig = Field(default_factory=SubscriptionServerDevConfig)
    qa: SubscriptionServerQaConfig = Field(default_factory=SubscriptionServerQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        SubscriptionServerMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=SubscriptionServerMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class SubscriptionServerConfigDict(TypedDict):
    production: NotRequired[SubscriptionServerProductionConfigDict]
    staging: NotRequired[SubscriptionServerStagingConfigDict]
    dev: NotRequired[SubscriptionServerDevConfigDict]
    qa: NotRequired[SubscriptionServerQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        SubscriptionServerMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class SoftwareManagementV1ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/fota/v1"


class SoftwareManagementV1ProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV1StagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/fota/v1"


class SoftwareManagementV1StagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV1DevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/fota/v1"


class SoftwareManagementV1DevConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV1QaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v1"


class SoftwareManagementV1QaConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV1MockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/fota/v1"


class SoftwareManagementV1MockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV1Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: SoftwareManagementV1ProductionConfig = Field(default_factory=SoftwareManagementV1ProductionConfig)
    staging: SoftwareManagementV1StagingConfig = Field(default_factory=SoftwareManagementV1StagingConfig)
    dev: SoftwareManagementV1DevConfig = Field(default_factory=SoftwareManagementV1DevConfig)
    qa: SoftwareManagementV1QaConfig = Field(default_factory=SoftwareManagementV1QaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        SoftwareManagementV1MockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=SoftwareManagementV1MockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class SoftwareManagementV1ConfigDict(TypedDict):
    production: NotRequired[SoftwareManagementV1ProductionConfigDict]
    staging: NotRequired[SoftwareManagementV1StagingConfigDict]
    dev: NotRequired[SoftwareManagementV1DevConfigDict]
    qa: NotRequired[SoftwareManagementV1QaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        SoftwareManagementV1MockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class SoftwareManagementV2ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/fota/v2"


class SoftwareManagementV2ProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV2StagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/fota/v2"


class SoftwareManagementV2StagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV2DevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/fota/v2"


class SoftwareManagementV2DevConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV2QaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v2"


class SoftwareManagementV2QaConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV2MockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/fota/v2"


class SoftwareManagementV2MockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: SoftwareManagementV2ProductionConfig = Field(default_factory=SoftwareManagementV2ProductionConfig)
    staging: SoftwareManagementV2StagingConfig = Field(default_factory=SoftwareManagementV2StagingConfig)
    dev: SoftwareManagementV2DevConfig = Field(default_factory=SoftwareManagementV2DevConfig)
    qa: SoftwareManagementV2QaConfig = Field(default_factory=SoftwareManagementV2QaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        SoftwareManagementV2MockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=SoftwareManagementV2MockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class SoftwareManagementV2ConfigDict(TypedDict):
    production: NotRequired[SoftwareManagementV2ProductionConfigDict]
    staging: NotRequired[SoftwareManagementV2StagingConfigDict]
    dev: NotRequired[SoftwareManagementV2DevConfigDict]
    qa: NotRequired[SoftwareManagementV2QaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        SoftwareManagementV2MockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class SoftwareManagementV3ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/fota/v3"


class SoftwareManagementV3ProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV3StagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/fota/v3"


class SoftwareManagementV3StagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV3DevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/fota/v3"


class SoftwareManagementV3DevConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV3QaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v3"


class SoftwareManagementV3QaConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV3MockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/fota/v3"


class SoftwareManagementV3MockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class SoftwareManagementV3Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: SoftwareManagementV3ProductionConfig = Field(default_factory=SoftwareManagementV3ProductionConfig)
    staging: SoftwareManagementV3StagingConfig = Field(default_factory=SoftwareManagementV3StagingConfig)
    dev: SoftwareManagementV3DevConfig = Field(default_factory=SoftwareManagementV3DevConfig)
    qa: SoftwareManagementV3QaConfig = Field(default_factory=SoftwareManagementV3QaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        SoftwareManagementV3MockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=SoftwareManagementV3MockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class SoftwareManagementV3ConfigDict(TypedDict):
    production: NotRequired[SoftwareManagementV3ProductionConfigDict]
    staging: NotRequired[SoftwareManagementV3StagingConfigDict]
    dev: NotRequired[SoftwareManagementV3DevConfigDict]
    qa: NotRequired[SoftwareManagementV3QaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        SoftwareManagementV3MockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class DeviceDiagnosticsProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/diagnostics/v1"


class DeviceDiagnosticsProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceDiagnosticsStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/diagnostics/v1"


class DeviceDiagnosticsStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceDiagnosticsDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/diagnostics/v1"


class DeviceDiagnosticsDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceDiagnosticsQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/diagnostics/v1"


class DeviceDiagnosticsQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceDiagnosticsMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/diagnostics/v1"


class DeviceDiagnosticsMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class DeviceDiagnosticsConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: DeviceDiagnosticsProductionConfig = Field(default_factory=DeviceDiagnosticsProductionConfig)
    staging: DeviceDiagnosticsStagingConfig = Field(default_factory=DeviceDiagnosticsStagingConfig)
    dev: DeviceDiagnosticsDevConfig = Field(default_factory=DeviceDiagnosticsDevConfig)
    qa: DeviceDiagnosticsQaConfig = Field(default_factory=DeviceDiagnosticsQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        DeviceDiagnosticsMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=DeviceDiagnosticsMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class DeviceDiagnosticsConfigDict(TypedDict):
    production: NotRequired[DeviceDiagnosticsProductionConfigDict]
    staging: NotRequired[DeviceDiagnosticsStagingConfigDict]
    dev: NotRequired[DeviceDiagnosticsDevConfigDict]
    qa: NotRequired[DeviceDiagnosticsQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        DeviceDiagnosticsMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class CloudConnectorProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/cc/v1"


class CloudConnectorProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class CloudConnectorStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/cc/v1"


class CloudConnectorStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class CloudConnectorDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/cc/v1"


class CloudConnectorDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class CloudConnectorQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/cc/v1"


class CloudConnectorQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class CloudConnectorMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/cc/v1"


class CloudConnectorMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class CloudConnectorConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: CloudConnectorProductionConfig = Field(default_factory=CloudConnectorProductionConfig)
    staging: CloudConnectorStagingConfig = Field(default_factory=CloudConnectorStagingConfig)
    dev: CloudConnectorDevConfig = Field(default_factory=CloudConnectorDevConfig)
    qa: CloudConnectorQaConfig = Field(default_factory=CloudConnectorQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        CloudConnectorMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=CloudConnectorMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class CloudConnectorConfigDict(TypedDict):
    production: NotRequired[CloudConnectorProductionConfigDict]
    staging: NotRequired[CloudConnectorStagingConfigDict]
    dev: NotRequired[CloudConnectorDevConfigDict]
    qa: NotRequired[CloudConnectorQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        CloudConnectorMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class HyperPreciseLocationProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/hyper-precise/v1"


class HyperPreciseLocationProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseLocationStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/hyper-precise/v1"


class HyperPreciseLocationStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseLocationDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com:80/hyper-precise/v1"


class HyperPreciseLocationDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseLocationQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/hyper-precise/v1"


class HyperPreciseLocationQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseLocationMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/hyper-precise/v1"


class HyperPreciseLocationMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class HyperPreciseLocationConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: HyperPreciseLocationProductionConfig = Field(default_factory=HyperPreciseLocationProductionConfig)
    staging: HyperPreciseLocationStagingConfig = Field(default_factory=HyperPreciseLocationStagingConfig)
    dev: HyperPreciseLocationDevConfig = Field(default_factory=HyperPreciseLocationDevConfig)
    qa: HyperPreciseLocationQaConfig = Field(default_factory=HyperPreciseLocationQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        HyperPreciseLocationMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=HyperPreciseLocationMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class HyperPreciseLocationConfigDict(TypedDict):
    production: NotRequired[HyperPreciseLocationProductionConfigDict]
    staging: NotRequired[HyperPreciseLocationStagingConfigDict]
    dev: NotRequired[HyperPreciseLocationDevConfigDict]
    qa: NotRequired[HyperPreciseLocationQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        HyperPreciseLocationMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class ServicesProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://5gedge.verizon.com/api/mec/services"


class ServicesProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServicesStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.5gedge.verizon.com/api/mec/services"


class ServicesStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServicesDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.5gedge.verizon.com:80/mec/services"


class ServicesDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServicesQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.5gedge.verizon.com/api/mec/services"


class ServicesQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServicesMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/mec/services"


class ServicesMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServicesConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ServicesProductionConfig = Field(default_factory=ServicesProductionConfig)
    staging: ServicesStagingConfig = Field(default_factory=ServicesStagingConfig)
    dev: ServicesDevConfig = Field(default_factory=ServicesDevConfig)
    qa: ServicesQaConfig = Field(default_factory=ServicesQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        ServicesMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=ServicesMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class ServicesConfigDict(TypedDict):
    production: NotRequired[ServicesProductionConfigDict]
    staging: NotRequired[ServicesStagingConfigDict]
    dev: NotRequired[ServicesDevConfigDict]
    qa: NotRequired[ServicesQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        ServicesMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class QualityOfServiceProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://thingspace.verizon.com/api/m2m/v1/devices"


class QualityOfServiceProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class QualityOfServiceStagingConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://staging.thingspace.verizon.com/api/m2m/v1/devices"


class QualityOfServiceStagingConfigDict(TypedDict):
    base_url: NotRequired[str]


class QualityOfServiceDevConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://devmanagement-staging.thingspace.verizon.com/api/m2m/v1/devices"


class QualityOfServiceDevConfigDict(TypedDict):
    base_url: NotRequired[str]


class QualityOfServiceQaConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/m2m/v1/devices"


class QualityOfServiceQaConfigDict(TypedDict):
    base_url: NotRequired[str]


class QualityOfServiceMockServerForLimitedAvailabilitySeeQuickStartConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://mock-staging.thingspace.verizon.com/api/m2m/v1/devices"


class QualityOfServiceMockServerForLimitedAvailabilitySeeQuickStartConfigDict(TypedDict):
    base_url: NotRequired[str]


class QualityOfServiceConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: QualityOfServiceProductionConfig = Field(default_factory=QualityOfServiceProductionConfig)
    staging: QualityOfServiceStagingConfig = Field(default_factory=QualityOfServiceStagingConfig)
    dev: QualityOfServiceDevConfig = Field(default_factory=QualityOfServiceDevConfig)
    qa: QualityOfServiceQaConfig = Field(default_factory=QualityOfServiceQaConfig)
    mock_server_for_limited_availability_see_quick_start: (
        QualityOfServiceMockServerForLimitedAvailabilitySeeQuickStartConfig
    ) = Field(default_factory=QualityOfServiceMockServerForLimitedAvailabilitySeeQuickStartConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "staging":
            staging = self.staging
            return UrlTemplate(base_url=staging.base_url, path=path)
        if environment == "dev":
            dev = self.dev
            return UrlTemplate(base_url=dev.base_url, path=path)
        if environment == "qa":
            qa = self.qa
            return UrlTemplate(base_url=qa.base_url, path=path)
        mock_server_for_limited_availability_see_quick_start = self.mock_server_for_limited_availability_see_quick_start
        return UrlTemplate(base_url=mock_server_for_limited_availability_see_quick_start.base_url, path=path)


class QualityOfServiceConfigDict(TypedDict):
    production: NotRequired[QualityOfServiceProductionConfigDict]
    staging: NotRequired[QualityOfServiceStagingConfigDict]
    dev: NotRequired[QualityOfServiceDevConfigDict]
    qa: NotRequired[QualityOfServiceQaConfigDict]
    mock_server_for_limited_availability_see_quick_start: NotRequired[
        QualityOfServiceMockServerForLimitedAvailabilitySeeQuickStartConfigDict
    ]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    hyper_precise_credentials: HyperPreciseCredentialsConfig = Field(default_factory=HyperPreciseCredentialsConfig)
    imp_server: ImpServerConfig = Field(default_factory=ImpServerConfig)
    thingspace: ThingspaceConfig = Field(default_factory=ThingspaceConfig)
    o_auth_server: OauthServerConfig = Field(default_factory=OauthServerConfig)
    m2_m: M2MConfig = Field(default_factory=M2MConfig)
    device_location: DeviceLocationConfig = Field(default_factory=DeviceLocationConfig)
    subscription_server: SubscriptionServerConfig = Field(default_factory=SubscriptionServerConfig)
    software_management_v1: SoftwareManagementV1Config = Field(default_factory=SoftwareManagementV1Config)
    software_management_v2: SoftwareManagementV2Config = Field(default_factory=SoftwareManagementV2Config)
    software_management_v3: SoftwareManagementV3Config = Field(default_factory=SoftwareManagementV3Config)
    device_diagnostics: DeviceDiagnosticsConfig = Field(default_factory=DeviceDiagnosticsConfig)
    cloud_connector: CloudConnectorConfig = Field(default_factory=CloudConnectorConfig)
    hyper_precise_location: HyperPreciseLocationConfig = Field(default_factory=HyperPreciseLocationConfig)
    services: ServicesConfig = Field(default_factory=ServicesConfig)
    quality_of_service: QualityOfServiceConfig = Field(default_factory=QualityOfServiceConfig)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    hyper_precise_credentials: NotRequired[HyperPreciseCredentialsConfigDict]
    imp_server: NotRequired[ImpServerConfigDict]
    thingspace: NotRequired[ThingspaceConfigDict]
    o_auth_server: NotRequired[OauthServerConfigDict]
    m2_m: NotRequired[M2MConfigDict]
    device_location: NotRequired[DeviceLocationConfigDict]
    subscription_server: NotRequired[SubscriptionServerConfigDict]
    software_management_v1: NotRequired[SoftwareManagementV1ConfigDict]
    software_management_v2: NotRequired[SoftwareManagementV2ConfigDict]
    software_management_v3: NotRequired[SoftwareManagementV3ConfigDict]
    device_diagnostics: NotRequired[DeviceDiagnosticsConfigDict]
    cloud_connector: NotRequired[CloudConnectorConfigDict]
    hyper_precise_location: NotRequired[HyperPreciseLocationConfigDict]
    services: NotRequired[ServicesConfigDict]
    quality_of_service: NotRequired[QualityOfServiceConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
