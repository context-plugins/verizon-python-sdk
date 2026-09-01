from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.campaign_meta_info_protocol import CampaignMetaInfoProtocolOrStr
from .v3_time_window import V3TimeWindow, V3TimeWindowDict


class V3CampaignMetaInfo(SdkBaseModel):
    """Campaign and campaign details."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    id: str
    """Campaign identifier."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Campaign name."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """Firmware name."""

    firmware_from: Optional[str] = Field(default=UNSET, alias="firmwareFrom")
    """Old firmware version."""

    firmware_to: Optional[str] = Field(default=UNSET, alias="firmwareTo")
    """New software version."""

    protocol: Optional[CampaignMetaInfoProtocolOrStr] = UNSET
    """Firmware protocol. Valid values include: LWM2M, OMD-DM."""

    make: str
    """Device make."""

    model: str
    """Device model."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    campaign_time_window_list: Optional[list[V3TimeWindow]] = Field(default=UNSET, alias="campaignTimeWindowList")
    """List of allowed campaign time windows."""

    status: str
    """Firmware upgrade status."""


class V3CampaignMetaInfoDict(TypedDict):
    account_name: str
    id: str
    campaign_name: NotRequired[str]
    firmware_name: NotRequired[str]
    firmware_from: NotRequired[str]
    firmware_to: NotRequired[str]
    protocol: NotRequired[CampaignMetaInfoProtocolOrStr]
    make: str
    model: str
    start_date: Date
    end_date: Date
    campaign_time_window_list: NotRequired[list[V3TimeWindow | V3TimeWindowDict]]
    status: str
