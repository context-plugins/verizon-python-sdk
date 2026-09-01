from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_service_request import DeviceServiceRequest, DeviceServiceRequestDict


class BullseyeServiceRequest(SdkBaseModel):
    """Account number and list of devices."""

    device_list: list[DeviceServiceRequest] = Field(alias="deviceList")
    """A list of devices."""

    account_number: str = Field(alias="accountNumber")
    """The numeric ID of the account and must include leading zeroes. This value is indentical to ``accountName``."""


class BullseyeServiceRequestDict(TypedDict):
    device_list: list[DeviceServiceRequest | DeviceServiceRequestDict]
    account_number: str
