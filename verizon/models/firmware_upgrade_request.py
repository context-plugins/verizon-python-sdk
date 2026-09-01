from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class FirmwareUpgradeRequest(SdkBaseModel):
    """Details of the firmware upgrade request."""

    account_name: str = Field(alias="accountName")
    """Account identifier in "##########-#####"."""

    firmware_name: str = Field(alias="firmwareName")
    """The name of the firmware image that will be used for the upgrade, from a GET /firmware response."""

    firmware_to: str = Field(alias="firmwareTo")
    """The name of the firmware version that will be on the devices after a successful upgrade."""

    start_date: Date = Field(alias="startDate")
    """The date that the upgrade begins."""

    end_date: Date = Field(alias="endDate")
    """The date that the upgrade ends."""

    device_list: list[str] = Field(alias="deviceList")
    """The IMEIs of the devices."""


class FirmwareUpgradeRequestDict(TypedDict):
    account_name: str
    firmware_name: str
    firmware_to: str
    start_date: Date
    end_date: Date
    device_list: list[str]
