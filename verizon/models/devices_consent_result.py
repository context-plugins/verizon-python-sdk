from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DevicesConsentResult(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    all_device: Optional[bool] = Field(default=UNSET, alias="allDevice")
    """Exclude all devices or not?"""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """Are there more devices to retrieve or not?"""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total number of excluded devices in the account."""

    update_time: Optional[str] = Field(default=UNSET, alias="updateTime")
    """Last update time."""

    exclusion: Optional[list[str]] = UNSET
    """Device ID list."""


class DevicesConsentResultDict(TypedDict):
    account_name: NotRequired[str]
    all_device: NotRequired[bool]
    has_more_data: NotRequired[bool]
    total_count: NotRequired[int]
    update_time: NotRequired[str]
    exclusion: NotRequired[list[str]]
