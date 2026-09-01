from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .v2_time_window import V2TimeWindow, V2TimeWindowDict


class CampaignSoftware(SdkBaseModel):
    """Software upgrade information."""

    id: str
    """Upgrade identifier."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """Campaign name."""

    software_name: str = Field(alias="softwareName")
    """Software name."""

    distribution_type: str = Field(alias="distributionType")
    """LWM2M, OMD-DM or HTTP."""

    make: str
    """Applicable make."""

    model: str
    """Applicable model."""

    software_from: str = Field(alias="softwareFrom")
    """Old software name."""

    software_to: str = Field(alias="softwareTo")
    """New software name."""

    start_date: Date = Field(alias="startDate")
    """Campaign start date."""

    end_date: Date = Field(alias="endDate")
    """Campaign end date."""

    download_after_date: Optional[Date] = Field(default=UNSET, alias="downloadAfterDate")
    """Specifies starting date client should download package. If null, client will download as soon as possible."""

    download_time_window_list: Optional[list[V2TimeWindow]] = Field(default=UNSET, alias="downloadTimeWindowList")
    """List of allowed download time windows."""

    install_after_date: Optional[Date] = Field(default=UNSET, alias="installAfterDate")
    """Client will install package after date. If null, client will install as soon as possible."""

    install_time_window_list: Optional[list[V2TimeWindow]] = Field(default=UNSET, alias="installTimeWindowList")
    """List of allowed install time windows."""

    status: str
    """Software upgrade status."""


class CampaignSoftwareDict(TypedDict):
    id: str
    account_name: str
    campaign_name: NotRequired[str]
    software_name: str
    distribution_type: str
    make: str
    model: str
    software_from: str
    software_to: str
    start_date: Date
    end_date: Date
    download_after_date: NotRequired[Date]
    download_time_window_list: NotRequired[list[V2TimeWindow | V2TimeWindowDict]]
    install_after_date: NotRequired[Date]
    install_time_window_list: NotRequired[list[V2TimeWindow | V2TimeWindowDict]]
    status: str
