from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V3AddOrRemoveDeviceRequest(SdkBaseModel):
    """Devices to add or remove from existing software upgrade information."""

    type_: str = Field(alias="Type")
    """Operation either 'append' or 'remove'"""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V3AddOrRemoveDeviceRequestDict(TypedDict):
    type_: str
    device_list: list[str]
