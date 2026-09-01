from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class V1ListOfLicensesToRemove(SdkBaseModel):
    """List of cancellation candidate devices."""

    count: Optional[int] = UNSET
    """The total number of devices on the list."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """True if there are more devices to retrieve."""

    update_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updateTime")
    """The date and time that the list was last updated."""

    device_list: Optional[list[str]] = Field(default=UNSET, alias="deviceList")
    """The IMEIs of the devices."""


class V1ListOfLicensesToRemoveDict(TypedDict):
    count: NotRequired[int]
    has_more_data: NotRequired[bool]
    update_time: NotRequired[RFC3339DateTime]
    device_list: NotRequired[list[str]]
