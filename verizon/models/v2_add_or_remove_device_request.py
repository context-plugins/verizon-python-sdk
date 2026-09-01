from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V2AddOrRemoveDeviceRequest(SdkBaseModel):
    """Add or remove device to existing software upgrade information."""

    type_: str = Field(alias="Type")
    """Operation either 'append' or 'remove'."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V2AddOrRemoveDeviceRequestDict(TypedDict):
    type_: str
    device_list: list[str]
