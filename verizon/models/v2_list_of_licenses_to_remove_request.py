from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V2ListOfLicensesToRemoveRequest(SdkBaseModel):
    """License cancellation candidate devices."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """List creation option."""

    count: Optional[int] = UNSET
    """The number of devices."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V2ListOfLicensesToRemoveRequestDict(TypedDict):
    type_: NotRequired[str]
    count: NotRequired[int]
    device_list: list[str]
