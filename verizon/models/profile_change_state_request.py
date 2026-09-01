from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class ProfileChangeStateRequest(SdkBaseModel):
    devices: list[DeviceList]
    account_name: str = Field(alias="accountName")
    smsr_oid: str = Field(alias="smsrOid")


class ProfileChangeStateRequestDict(TypedDict):
    devices: list[DeviceList | DeviceListDict]
    account_name: str
    smsr_oid: str
