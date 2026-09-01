from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .hpl_bullseye_enable import HplBullseyeEnable, HplBullseyeEnableDict


class DeviceServiceRequest(SdkBaseModel):
    """Device information."""

    imei: str
    """The International Mobile Equipment Identifier of the device."""

    bullseye_enable: HplBullseyeEnable = Field(alias="BullseyeEnable")
    """A flag that shows if Hyper Precise is enabled (true) or disabled (false)."""


class DeviceServiceRequestDict(TypedDict):
    imei: str
    bullseye_enable: HplBullseyeEnable | HplBullseyeEnableDict
