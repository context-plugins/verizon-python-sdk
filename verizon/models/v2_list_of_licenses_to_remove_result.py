from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V2ListOfLicensesToRemoveResult(SdkBaseModel):
    """List of created license cancellation devices."""

    count: int
    """The number of devices."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V2ListOfLicensesToRemoveResultDict(TypedDict):
    count: int
    device_list: list[str]
