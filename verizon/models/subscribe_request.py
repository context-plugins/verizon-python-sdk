from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .qosdevice_info import QosdeviceInfo, QosdeviceInfoDict


class SubscribeRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    device_info: list[QosdeviceInfo] = Field(alias="deviceInfo")


class SubscribeRequestDict(TypedDict):
    account_name: str
    device_info: list[QosdeviceInfo | QosdeviceInfoDict]
