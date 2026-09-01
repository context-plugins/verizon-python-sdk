from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download_time_window import DownloadTimeWindow, DownloadTimeWindowDict


class SchedulesSoftwareUpgradeRequest(SdkBaseModel):
    campaign_name: Optional[str] = Field(default=UNSET, alias="campaignName")
    """The campaign name."""

    software_name: Optional[str] = Field(default=UNSET, alias="softwareName")
    """Software name."""

    software_from: Optional[str] = Field(default=UNSET, alias="softwareFrom")
    """Old software name."""

    software_to: Optional[str] = Field(default=UNSET, alias="softwareTo")
    """New software name."""

    distribution_type: Optional[str] = Field(default=UNSET, alias="distributionType")
    """Valid values"""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Campaign start date."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """Campaign end date."""

    download_after_date: Optional[str] = Field(default=UNSET, alias="downloadAfterDate")
    """Specifies the starting date the client should download the package. If null, client downloads as soon as
    possible."""

    download_time_window_list: Optional[list[DownloadTimeWindow]] = Field(default=UNSET, alias="downloadTimeWindowList")
    """List of allowed download time windows."""

    install_after_date: Optional[str] = Field(default=UNSET, alias="installAfterDate")
    """The date after which you install the package. If null, install as soon as possible."""

    install_time_window_list: Optional[list[DownloadTimeWindow]] = Field(default=UNSET, alias="installTimeWindowList")
    """List of allowed install time windows."""

    device_list: Optional[list[str]] = Field(default=UNSET, alias="deviceList")
    """Device IMEI list."""


class SchedulesSoftwareUpgradeRequestDict(TypedDict):
    campaign_name: NotRequired[str]
    software_name: NotRequired[str]
    software_from: NotRequired[str]
    software_to: NotRequired[str]
    distribution_type: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    download_after_date: NotRequired[str]
    download_time_window_list: NotRequired[list[DownloadTimeWindow | DownloadTimeWindowDict]]
    install_after_date: NotRequired[str]
    install_time_window_list: NotRequired[list[DownloadTimeWindow | DownloadTimeWindowDict]]
    device_list: NotRequired[list[str]]
