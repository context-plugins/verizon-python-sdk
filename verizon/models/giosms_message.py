from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class GiosmsMessage(SdkBaseModel):
    device_ids: Optional[list[GiodeviceId]] = Field(default=UNSET, alias="deviceIds")
    message: Optional[str] = UNSET
    timestamp: Optional[RFC3339DateTime] = UNSET


class GiosmsMessageDict(TypedDict):
    device_ids: NotRequired[list[GiodeviceId | GiodeviceIdDict]]
    message: NotRequired[str]
    timestamp: NotRequired[RFC3339DateTime]
