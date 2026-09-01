from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict


class DeviceActivationRequest(SdkBaseModel):
    """Request for device status to check availability of activation."""

    account_name: str = Field(alias="accountName")
    """The name of a billing account."""

    devices: list[AccountDeviceList]
    """Up to 10,000 devices that you want to move to a different account, specified by device identifier."""


class DeviceActivationRequestDict(TypedDict):
    account_name: str
    devices: list[AccountDeviceList | AccountDeviceListDict]
