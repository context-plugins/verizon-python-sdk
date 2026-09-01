from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1ListOfLicensesToRemoveResult(SdkBaseModel):
    """List of licenses assigned."""

    count: Optional[int] = UNSET
    """The total number of devices on the cancellation candidate list."""

    device_list: Optional[list[str]] = Field(default=UNSET, alias="deviceList")
    """The IMEIs of the devices."""


class V1ListOfLicensesToRemoveResultDict(TypedDict):
    count: NotRequired[int]
    device_list: NotRequired[list[str]]
