from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v2_device_status import V2DeviceStatus, V2DeviceStatusDict


class V2LicensesAssignedRemovedResult(SdkBaseModel):
    """License assignment or removal confirmation."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    lic_total_count: int = Field(alias="licTotalCount")
    """Total license count."""

    lic_used_count: int = Field(alias="licUsedCount")
    """Assigned license count."""

    device_list: list[V2DeviceStatus] = Field(alias="deviceList")
    """List of devices with id in IMEI."""


class V2LicensesAssignedRemovedResultDict(TypedDict):
    account_name: str
    lic_total_count: int
    lic_used_count: int
    device_list: list[V2DeviceStatus | V2DeviceStatusDict]
