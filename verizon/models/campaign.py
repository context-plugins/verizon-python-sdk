from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v3_time_window import V3TimeWindow, V3TimeWindowDict


class Campaign(SdkBaseModel):
    """Firmware upgrade information."""

    id: str
    """Upgrade identifier."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Campaign name."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """Name of firmware."""

    firmware_from: Optional[str] = Field(default=UNSET, alias="firmwareFrom")
    """Old firmware version."""

    firmware_to: Optional[str] = Field(default=UNSET, alias="firmwareTo")
    """New firmware version."""

    protocol: str
    """The protocol of the firmware distribution. Default: LWM2M."""

    make: str
    """Applicable make."""

    model: str
    """Applicable model."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    campaign_time_window_list: Optional[list[V3TimeWindow]] = Field(default=UNSET, alias="campaignTimeWindowList")
    """List of allowed campaign time windows."""

    status: str
    """Firmware upgrade status."""

    auto_assign_license_flag: bool = Field(alias="autoAssignLicenseFlag")
    """Any device included in the device list which does not have a license will automatically be assigned a FOTA
    license, assuming there are enough FOTA licenses available, when set to true."""

    auto_add_devices_flag: bool = Field(alias="autoAddDevicesFlag")
    """Beyond the devices included on the device list, any other device(s) which matches the eligibility criteria (same
    make, model, current firmware, protocol, billing account) will automatically be added to the campaign list during
    the life of the campaign when set to true."""


class CampaignDict(TypedDict):
    id: str
    account_name: str
    campaign_name: NotRequired[str]
    firmware_name: NotRequired[str]
    firmware_from: NotRequired[str]
    firmware_to: NotRequired[str]
    protocol: str
    make: str
    model: str
    start_date: Date
    end_date: Date
    campaign_time_window_list: NotRequired[list[V3TimeWindow | V3TimeWindowDict]]
    status: str
    auto_assign_license_flag: bool
    auto_add_devices_flag: bool
