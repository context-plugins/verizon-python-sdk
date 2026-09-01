from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class DeviceProvisioningHistoryListRequest(SdkBaseModel):
    """Request to return the provisioning history of a specified device during a specified time period."""

    device_id: DeviceId = Field(alias="deviceId")
    """An identifier for a single device."""

    earliest: str
    """The earliest date and time for which you want provisioning data."""

    latest: str
    """The last date and time for which you want provisioning data."""


class DeviceProvisioningHistoryListRequestDict(TypedDict):
    device_id: DeviceId | DeviceIdDict
    earliest: str
    latest: str
