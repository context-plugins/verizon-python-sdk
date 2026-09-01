from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectionResponse(SdkBaseModel):
    """response for /clients/connection"""

    mqtt_url: str = Field(alias="MqttURL")
    """The full MQTT URL including protocol, host, and port."""

    host: Optional[str] = Field(default=UNSET, alias="Host")
    """The hostname of the MQTT broker to connect to."""

    port: Optional[int] = Field(default=UNSET, alias="Port")
    """The port number of the MQTT broker."""


class ConnectionResponseDict(TypedDict):
    mqtt_url: str
    host: NotRequired[str]
    port: NotRequired[int]
