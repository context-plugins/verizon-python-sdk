from __future__ import annotations

from dataclasses import dataclass

from ..core import UrlTemplate
from .environment import Environment
from .server_config import ServerConfig


@dataclass(frozen=True, slots=True)
class Server:
    environment: Environment
    config: ServerConfig

    def hyper_precise_credentials(self, path: str) -> UrlTemplate:
        return self.config.hyper_precise_credentials.resolve(self.environment, path)

    def imp_server(self, path: str) -> UrlTemplate:
        return self.config.imp_server.resolve(self.environment, path)

    def thingspace(self, path: str) -> UrlTemplate:
        return self.config.thingspace.resolve(self.environment, path)

    def o_auth_server(self, path: str) -> UrlTemplate:
        return self.config.o_auth_server.resolve(self.environment, path)

    def m2_m(self, path: str) -> UrlTemplate:
        return self.config.m2_m.resolve(self.environment, path)

    def device_location(self, path: str) -> UrlTemplate:
        return self.config.device_location.resolve(self.environment, path)

    def subscription_server(self, path: str) -> UrlTemplate:
        return self.config.subscription_server.resolve(self.environment, path)

    def software_management_v1(self, path: str) -> UrlTemplate:
        return self.config.software_management_v1.resolve(self.environment, path)

    def software_management_v2(self, path: str) -> UrlTemplate:
        return self.config.software_management_v2.resolve(self.environment, path)

    def software_management_v3(self, path: str) -> UrlTemplate:
        return self.config.software_management_v3.resolve(self.environment, path)

    def device_diagnostics(self, path: str) -> UrlTemplate:
        return self.config.device_diagnostics.resolve(self.environment, path)

    def cloud_connector(self, path: str) -> UrlTemplate:
        return self.config.cloud_connector.resolve(self.environment, path)

    def hyper_precise_location(self, path: str) -> UrlTemplate:
        return self.config.hyper_precise_location.resolve(self.environment, path)

    def services(self, path: str) -> UrlTemplate:
        return self.config.services.resolve(self.environment, path)

    def quality_of_service(self, path: str) -> UrlTemplate:
        return self.config.quality_of_service.resolve(self.environment, path)
