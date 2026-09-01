from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_response_code import ApiResponseCode, ApiResponseCodeDict
from .device_service_information import DeviceServiceInformation, DeviceServiceInformationDict


class BullseyeServiceResult(SdkBaseModel):
    """Status of Hyper Precise Location on the device."""

    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric ID of the account and must include leading zeroes. This value is indentical to ``accountName``."""

    device_list: Optional[list[DeviceServiceInformation]] = Field(default=UNSET, alias="deviceList")
    """List of devices."""

    response_type: Optional[ApiResponseCode] = Field(default=UNSET, alias="responseType")
    """ResponseCode and/or a message indicating success or failure of the request."""


class BullseyeServiceResultDict(TypedDict):
    account_number: NotRequired[str]
    device_list: NotRequired[list[DeviceServiceInformation | DeviceServiceInformationDict]]
    response_type: NotRequired[ApiResponseCode | ApiResponseCodeDict]
