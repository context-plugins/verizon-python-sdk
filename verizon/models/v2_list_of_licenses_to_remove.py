from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V2ListOfLicensesToRemove(SdkBaseModel):
    """A list of license cancellation candidate devices."""

    count: int
    """Cancellation candidate devices count."""

    has_more_data: bool = Field(alias="hasMoreData")
    """Flag to indicat more devices."""

    update_time: str = Field(alias="updateTime")
    """Last update time."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V2ListOfLicensesToRemoveDict(TypedDict):
    count: int
    has_more_data: bool
    update_time: str
    device_list: list[str]
