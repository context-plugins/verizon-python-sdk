from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class ProvhistoryRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    device_filter: Optional[list[GiodeviceId]] = Field(default=UNSET, alias="deviceFilter")
    earliest: Optional[RFC3339DateTime] = UNSET
    latest: Optional[RFC3339DateTime] = UNSET


class ProvhistoryRequestDict(TypedDict):
    account_name: NotRequired[str]
    device_filter: NotRequired[list[GiodeviceId | GiodeviceIdDict]]
    earliest: NotRequired[RFC3339DateTime]
    latest: NotRequired[RFC3339DateTime]
