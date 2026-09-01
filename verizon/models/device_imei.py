from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceImei(SdkBaseModel):
    """Device IMEI list."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class DeviceImeiDict(TypedDict):
    device_list: list[str]
