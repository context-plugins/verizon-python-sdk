from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v3_time_window import V3TimeWindow, V3TimeWindowDict


class CampaignFirmwareUpgrade(SdkBaseModel):
    """Firmware upgrade for devices."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Campaign name."""

    firmware_name: str = Field(alias="firmwareName")
    """Firmware name to upgrade to."""

    firmware_from: str = Field(alias="firmwareFrom")
    """Old firmware version."""

    firmware_to: str = Field(alias="firmwareTo")
    """New firmware version."""

    protocol: str
    """Valid values include: LWM2M, OMA and HTTP."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    campaign_time_window_list: Optional[list[V3TimeWindow]] = Field(default=UNSET, alias="campaignTimeWindowList")
    """List of allowed campaign time windows."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""

    auto_assign_license_flag: bool = Field(alias="autoAssignLicenseFlag")
    """This flag, when set to true, will assign a FOTA license automatically if the device does not have one already."""

    auto_add_devices_flag: bool = Field(alias="autoAddDevicesFlag")
    """this flag, when set to true, will automatically add a device of the same make and model to a campaign."""


class CampaignFirmwareUpgradeDict(TypedDict):
    campaign_name: NotRequired[str]
    firmware_name: str
    firmware_from: str
    firmware_to: str
    protocol: str
    start_date: Date
    end_date: Date
    campaign_time_window_list: NotRequired[list[V3TimeWindow | V3TimeWindowDict]]
    device_list: list[str]
    auto_assign_license_flag: bool
    auto_add_devices_flag: bool
