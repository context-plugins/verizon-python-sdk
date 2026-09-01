from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pwndevice_id import PwndeviceId, PwndeviceIdDict


class PwndeviceList(SdkBaseModel):
    device_ids: list[PwndeviceId] = Field(alias="deviceIds")


class PwndeviceListDict(TypedDict):
    device_ids: list[PwndeviceId | PwndeviceIdDict]
