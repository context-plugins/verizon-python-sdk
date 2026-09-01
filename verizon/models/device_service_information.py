from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_response_code import ApiResponseCode, ApiResponseCodeDict
from .hpl_bullseye_enable import HplBullseyeEnable, HplBullseyeEnableDict


class DeviceServiceInformation(SdkBaseModel):
    """Device service information."""

    response_type: Optional[ApiResponseCode] = Field(default=UNSET, alias="responseType")
    """ResponseCode and/or a message indicating success or failure of the request."""

    imei: str
    """The International Mobile Equipment Identifier of the device."""

    bullseye_enable: HplBullseyeEnable = Field(alias="BullseyeEnable")
    """A flag that shows if Hyper Precise is enabled (true) or disabled (false)."""


class DeviceServiceInformationDict(TypedDict):
    response_type: NotRequired[ApiResponseCode | ApiResponseCodeDict]
    imei: str
    bullseye_enable: HplBullseyeEnable | HplBullseyeEnableDict
