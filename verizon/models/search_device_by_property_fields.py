from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .acceleration import Acceleration, AccelerationDict
from .device_propertylocation import DevicePropertylocation, DevicePropertylocationDict


class SearchDeviceByPropertyFields(SdkBaseModel):
    """List of device sensors and their most recently reported values."""

    acceleration: Optional[Acceleration] = UNSET
    battery: Optional[str] = UNSET
    humidity: Optional[str] = UNSET
    light: Optional[str] = UNSET
    pressure: Optional[str] = UNSET
    signal_strength: Optional[str] = Field(default=UNSET, alias="signalStrength")
    temperature: Optional[str] = UNSET
    device_propertylocation: Optional[DevicePropertylocation] = Field(default=UNSET, alias="DevicePropertylocation")


class SearchDeviceByPropertyFieldsDict(TypedDict):
    acceleration: NotRequired[Acceleration | AccelerationDict]
    battery: NotRequired[str]
    humidity: NotRequired[str]
    light: NotRequired[str]
    pressure: NotRequired[str]
    signal_strength: NotRequired[str]
    temperature: NotRequired[str]
    device_propertylocation: NotRequired[DevicePropertylocation | DevicePropertylocationDict]
