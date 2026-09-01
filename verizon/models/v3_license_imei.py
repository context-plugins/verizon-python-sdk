from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V3LicenseImei(SdkBaseModel):
    """List of devices."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V3LicenseImeiDict(TypedDict):
    device_list: list[str]
