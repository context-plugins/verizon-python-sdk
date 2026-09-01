from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v3_device import V3Device, V3DeviceDict


class DeviceListResult(SdkBaseModel):
    """Device list information."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    device_count: int = Field(alias="deviceCount")
    """Total device count."""

    device_list: list[V3Device] = Field(alias="deviceList")
    """List of devices with id in IMEI."""


class DeviceListResultDict(TypedDict):
    account_name: str
    device_count: int
    device_list: list[V3Device | V3DeviceDict]
