from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class SmseventHistoryRequest(SdkBaseModel):
    device_id: GiodeviceId = Field(alias="deviceId")
    earliest: Optional[RFC3339DateTime] = UNSET
    latest: Optional[RFC3339DateTime] = UNSET


class SmseventHistoryRequestDict(TypedDict):
    device_id: GiodeviceId | GiodeviceIdDict
    earliest: NotRequired[RFC3339DateTime]
    latest: NotRequired[RFC3339DateTime]
