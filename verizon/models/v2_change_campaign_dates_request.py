from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v2_time_window import V2TimeWindow, V2TimeWindowDict


class V2ChangeCampaignDatesRequest(SdkBaseModel):
    """New dates and time windows."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    download_after_date: Optional[Date] = Field(default=UNSET, alias="downloadAfterDate")
    """Specifies starting date client should download package. If null, client will download as soon as possible."""

    download_time_window_list: Optional[list[V2TimeWindow]] = Field(default=UNSET, alias="downloadTimeWindowList")
    """List of allowed download time windows. Removing of existing windows is not allowed."""

    install_after_date: Optional[Date] = Field(default=UNSET, alias="installAfterDate")
    """Client will install package after date. If null, client will install as soon as possible."""

    install_time_window_list: Optional[list[V2TimeWindow]] = Field(default=UNSET, alias="installTimeWindowList")
    """List of allowed install time windows. Removing of existing windows is not allowed."""


class V2ChangeCampaignDatesRequestDict(TypedDict):
    start_date: Date
    end_date: Date
    download_after_date: NotRequired[Date]
    download_time_window_list: NotRequired[list[V2TimeWindow | V2TimeWindowDict]]
    install_after_date: NotRequired[Date]
    install_time_window_list: NotRequired[list[V2TimeWindow | V2TimeWindowDict]]
