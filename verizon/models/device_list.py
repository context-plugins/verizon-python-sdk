from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class DeviceList(SdkBaseModel):
    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")


class DeviceListDict(TypedDict):
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
