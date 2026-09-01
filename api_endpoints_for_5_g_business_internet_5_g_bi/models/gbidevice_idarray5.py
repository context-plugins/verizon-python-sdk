from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_id import DeviceId, DeviceIdDict


class GbideviceIdarray5(SdkBaseModel):
    device_id: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceId")


class GbideviceIdarray5Dict(TypedDict):
    device_id: NotRequired[list[DeviceId | DeviceIdDict]]
