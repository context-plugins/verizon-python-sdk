from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_identifier import DeviceIdentifier, DeviceIdentifierDict


class GetDeviceExperienceScoreHistoryRequest(SdkBaseModel):
    """Get device experience score history."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    device_id: DeviceIdentifier = Field(alias="deviceId")
    """Device Id details."""


class GetDeviceExperienceScoreHistoryRequestDict(TypedDict):
    account_name: str
    device_id: DeviceIdentifier | DeviceIdentifierDict
