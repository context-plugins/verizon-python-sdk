from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v3_time_window import V3TimeWindow, V3TimeWindowDict


class V3ChangeCampaignDatesRequest(SdkBaseModel):
    """Campaign dates and time windows."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    campaign_time_window_list: Optional[list[V3TimeWindow]] = Field(default=UNSET, alias="campaignTimeWindowList")
    """List of allowed campaign time windows."""


class V3ChangeCampaignDatesRequestDict(TypedDict):
    start_date: Date
    end_date: Date
    campaign_time_window_list: NotRequired[list[V3TimeWindow | V3TimeWindowDict]]
