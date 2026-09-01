from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pwndevice_id import PwndeviceId, PwndeviceIdDict


class DeviceListIp(SdkBaseModel):
    device_ids: list[PwndeviceId] = Field(alias="deviceIds")
    ip_address: str = Field(alias="ipAddress")


class DeviceListIpDict(TypedDict):
    device_ids: list[PwndeviceId | PwndeviceIdDict]
    ip_address: str
