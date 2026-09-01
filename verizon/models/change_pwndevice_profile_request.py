from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pwndevice_list import PwndeviceList, PwndeviceListDict


class ChangePwndeviceProfileRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    device_list: list[PwndeviceList] = Field(alias="deviceList")
    new_profile: str = Field(alias="newProfile")


class ChangePwndeviceProfileRequestDict(TypedDict):
    account_name: str
    device_list: list[PwndeviceList | PwndeviceListDict]
    new_profile: str
