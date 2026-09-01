from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_list_ip import DeviceListIp, DeviceListIpDict


class ChangePwndeviceIpaddressRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    device_list: list[DeviceListIp] = Field(alias="deviceList")


class ChangePwndeviceIpaddressRequestDict(TypedDict):
    account_name: str
    device_list: list[DeviceListIp | DeviceListIpDict]
