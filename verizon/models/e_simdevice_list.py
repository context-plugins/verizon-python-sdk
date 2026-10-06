from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_id1 import DeviceId1, DeviceId1Dict


class ESimdeviceList(SdkBaseModel):
    device_ids: Optional[list[DeviceId1]] = Field(default=UNSET, alias="deviceIds")


class ESimdeviceListDict(TypedDict):
    device_ids: NotRequired[list[DeviceId1Dict]]
