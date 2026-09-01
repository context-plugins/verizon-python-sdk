from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v3_time_window import V3TimeWindow, V3TimeWindowDict


class FirmwareCampaign(SdkBaseModel):
    """Firmware upgrade information."""

    id: str
    """Upgrade identifier."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Campaign name."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """Firmware name (for firmware upgrade only)."""

    firmware_from: str = Field(alias="firmwareFrom")
    """Old firmware version (for firmware upgrade only)."""

    firmware_to: str = Field(alias="firmwareTo")
    """New firmware version (for firmware upgrade only)."""

    protocol: str
    """Available values: LWM2M."""

    make: str
    model: str
    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    campaign_time_window_list: Optional[list[V3TimeWindow]] = Field(default=UNSET, alias="campaignTimeWindowList")
    """List of allowed campaign time windows."""

    status: str
    """Campaign status."""


class FirmwareCampaignDict(TypedDict):
    id: str
    account_name: str
    campaign_name: NotRequired[str]
    firmware_name: NotRequired[str]
    firmware_from: str
    firmware_to: str
    protocol: str
    make: str
    model: str
    start_date: Date
    end_date: Date
    campaign_time_window_list: NotRequired[list[V3TimeWindow | V3TimeWindowDict]]
    status: str
