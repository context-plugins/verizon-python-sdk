from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectionResponseV3(SdkBaseModel):
    """response for api/v3/clients/connection"""

    mqtt_urls: list[str] = Field(alias="MqttURLs")
    """Array of full MQTT URLs including protocol, host, and port for each available MEC."""

    hosts: Optional[list[str]] = Field(default=UNSET, alias="Hosts")
    """Array of hostnames corresponding to each MQTT URL."""

    ports: Optional[list[int]] = Field(default=UNSET, alias="Ports")
    """Array of port numbers corresponding to each MQTT URL."""


class ConnectionResponseV3Dict(TypedDict):
    mqtt_urls: list[str]
    hosts: NotRequired[list[str]]
    ports: NotRequired[list[int]]
