from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class DeviceUploadRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    devices: list[DeviceList]
    email_address: str = Field(alias="emailAddress")
    device_sku: str = Field(alias="deviceSku")
    upload_type: str = Field(alias="uploadType")


class DeviceUploadRequestDict(TypedDict):
    account_name: str
    devices: list[DeviceList | DeviceListDict]
    email_address: str
    device_sku: str
    upload_type: str
