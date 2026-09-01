from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .activate import Activate, ActivateDict
from .pwndevice_list import PwndeviceList, PwndeviceListDict


class ChangePwndeviceStateActivateRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    device_list: list[PwndeviceList] = Field(alias="deviceList")
    activate: Activate


class ChangePwndeviceStateActivateRequestDict(TypedDict):
    account_name: str
    device_list: list[PwndeviceList | PwndeviceListDict]
    activate: Activate | ActivateDict
