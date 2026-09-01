from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .firmware_upgrade_device_list_item import FirmwareUpgradeDeviceListItem, FirmwareUpgradeDeviceListItemDict


class FirmwareUpgrade(SdkBaseModel):
    """Array of upgrade objects with the specified status."""

    id: Optional[str] = UNSET
    """The unique identifier for this upgrade."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """The name of the firmware image that will be used for the upgrade."""

    firmware_to: Optional[str] = Field(default=UNSET, alias="firmwareTo")
    """The name of the firmware version that will be on the devices after a successful upgrade."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """The intended start date for the upgrade."""

    status: Optional[str] = UNSET
    """The current status of the upgrade."""

    device_list: Optional[list[FirmwareUpgradeDeviceListItem]] = Field(default=UNSET, alias="deviceList")
    """A JSON object for each device that was included in the upgrade, showing the device IMEI, the status of the
    upgrade, and additional information about the status."""


class FirmwareUpgradeDict(TypedDict):
    id: NotRequired[str]
    account_name: NotRequired[str]
    firmware_name: NotRequired[str]
    firmware_to: NotRequired[str]
    start_date: NotRequired[str]
    status: NotRequired[str]
    device_list: NotRequired[list[FirmwareUpgradeDeviceListItem | FirmwareUpgradeDeviceListItemDict]]
