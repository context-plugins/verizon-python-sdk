from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourceOnBoardSensor(SdkBaseModel):
    deveui: str
    """the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer"""

    appeui: str
    """global application ID in IEEE EUI64 address space that uniquely identifies the entity able to process the JoinReq
    frame"""

    appkey: str
    """an encryption key used for messages during every over the air activation"""

    class_: str = Field(alias="class")
    """Class of the sensor device. Valid values are Class A (A), Class B (B), and Class C (C). All LoRaWAN devices must
    implement Class A"""

    kind: str
    """The kind of sensor device"""

    description: str
    name: str
    customdata: Optional[dict[str, Any]] = UNSET
    """Name/value pair, where the value is client defined. The purpose is to keep track of current state per device
    action."""


class ResourceOnBoardSensorDict(TypedDict):
    deveui: str
    appeui: str
    appkey: str
    class_: str
    kind: str
    description: str
    name: str
    customdata: NotRequired[dict[str, Any]]
