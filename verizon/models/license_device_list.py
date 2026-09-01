from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .license_device_id import LicenseDeviceId, LicenseDeviceIdDict


class LicenseDeviceList(SdkBaseModel):
    """List of all devices."""

    device_ids: Optional[list[LicenseDeviceId]] = Field(default=UNSET, alias="deviceIds")
    """For 4G devices, IMEI (decimal, up to 15 digits)."""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")


class LicenseDeviceListDict(TypedDict):
    device_ids: NotRequired[list[LicenseDeviceId | LicenseDeviceIdDict]]
    ip_address: NotRequired[str]
