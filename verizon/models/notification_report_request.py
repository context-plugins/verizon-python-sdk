from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class NotificationReportRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    request_type: str = Field(alias="requestType")
    devices: list[DeviceList]
    monitor_expiration_time: str = Field(alias="monitorExpirationTime")


class NotificationReportRequestDict(TypedDict):
    account_name: str
    request_type: str
    devices: list[DeviceList | DeviceListDict]
    monitor_expiration_time: str
