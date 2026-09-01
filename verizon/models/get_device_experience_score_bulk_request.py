from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_identifier import DeviceIdentifier, DeviceIdentifierDict


class GetDeviceExperienceScoreBulkRequest(SdkBaseModel):
    """Get device experience score bulk request."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    device_list: list[DeviceIdentifier] = Field(alias="deviceList")


class GetDeviceExperienceScoreBulkRequestDict(TypedDict):
    account_name: str
    device_list: list[DeviceIdentifier | DeviceIdentifierDict]
