from __future__ import annotations

from dataclasses import dataclass

from ..core import UrlTemplate
from .environment import Environment
from .server_config import ServerConfig


@dataclass(frozen=True, slots=True)
class Server:
    environment: Environment
    config: ServerConfig

    def o_auth_server(self, path: str) -> UrlTemplate:
        return self.config.o_auth_server.resolve(self.environment, path)

    def thingspace(self, path: str) -> UrlTemplate:
        return self.config.thingspace.resolve(self.environment, path)
