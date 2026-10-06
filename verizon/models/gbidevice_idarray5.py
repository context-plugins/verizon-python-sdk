from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_id1 import DeviceId1, DeviceId1Dict


class GbideviceIdarray5(SdkBaseModel):
    device_id: Optional[list[DeviceId1]] = Field(default=UNSET, alias="deviceId")


class GbideviceIdarray5Dict(TypedDict):
    device_id: NotRequired[list[DeviceId1Dict]]
