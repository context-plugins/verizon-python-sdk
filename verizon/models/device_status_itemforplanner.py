from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .device_idforplanner import DeviceIdforplanner, DeviceIdforplannerDict


class DeviceStatusItemforplanner(SdkBaseModel):
    device_ids: OptionalNullable[list[DeviceIdforplanner]] = Field(default=UNSET, alias="deviceIds")
    status: OptionalNullable[str] = UNSET
    reason: OptionalNullable[str] = UNSET


class DeviceStatusItemforplannerDict(TypedDict):
    device_ids: NotRequired[list[DeviceIdforplannerDict] | None]
    status: NotRequired[str | None]
    reason: NotRequired[str | None]
