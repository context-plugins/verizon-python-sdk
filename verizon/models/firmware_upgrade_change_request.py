from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.firmware_type_list import FirmwareTypeListOrStr


class FirmwareUpgradeChangeRequest(SdkBaseModel):
    """List of devices to add or remove."""

    type_: FirmwareTypeListOrStr = Field(alias="type")
    """Possible values are ``append`` or ``remove``"""

    device_list: list[str] = Field(alias="deviceList")
    """The IMEIs of the devices."""


class FirmwareUpgradeChangeRequestDict(TypedDict):
    type_: FirmwareTypeListOrStr
    device_list: list[str]
