from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict


class RetrieveMonitorsRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """The name of a billing account."""

    devices: list[AccountDeviceList]
    """The devices for which you want to restore service, specified by device identifier."""

    monitor_type: Optional[str] = Field(default=UNSET, alias="monitorType")
    """The name of a billing account."""


class RetrieveMonitorsRequestDict(TypedDict):
    account_name: str
    devices: list[AccountDeviceList | AccountDeviceListDict]
    monitor_type: NotRequired[str]
