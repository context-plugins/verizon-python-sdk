from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class StopMonitorRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    devices: list[DeviceList]


class StopMonitorRequestDict(TypedDict):
    account_name: str
    devices: list[DeviceList | DeviceListDict]
