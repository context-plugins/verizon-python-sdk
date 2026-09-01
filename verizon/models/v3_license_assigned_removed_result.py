from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v3_device_status import V3DeviceStatus, V3DeviceStatusDict


class V3LicenseAssignedRemovedResult(SdkBaseModel):
    """License assignment/removal response."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    lic_count: int = Field(alias="licCount")
    """Total license count."""

    lic_used_count: int = Field(alias="licUsedCount")
    """Assigned license count."""

    device_list: list[V3DeviceStatus] = Field(alias="deviceList")
    """List of devices with id in IMEI."""


class V3LicenseAssignedRemovedResultDict(TypedDict):
    account_name: str
    lic_count: int
    lic_used_count: int
    device_list: list[V3DeviceStatus | V3DeviceStatusDict]
