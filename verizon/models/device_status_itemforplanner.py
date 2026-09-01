from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_idforplanner import DeviceIdforplanner, DeviceIdforplannerDict


class DeviceStatusItemforplanner(SdkBaseModel):
    device_ids: Optional[list[DeviceIdforplanner | None]] = Field(default=UNSET, alias="deviceIds")
    status: OptionalNullable[str] = UNSET
    reason: OptionalNullable[str] = UNSET


class DeviceStatusItemforplannerDict(TypedDict):
    device_ids: NotRequired[list[DeviceIdforplanner | DeviceIdforplannerDict | None]]
    status: NotRequired[str | None]
    reason: NotRequired[str | None]
