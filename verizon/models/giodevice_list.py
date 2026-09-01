from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class GiodeviceList(SdkBaseModel):
    device_ids: Optional[list[GiodeviceId]] = Field(default=UNSET, alias="deviceIds")


class GiodeviceListDict(TypedDict):
    device_ids: NotRequired[list[GiodeviceId | GiodeviceIdDict]]
