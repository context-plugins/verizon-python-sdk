from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .device_id2 import DeviceId2, DeviceId2Dict


class ESimprovhistoryRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    device_filter: Optional[list[DeviceId2]] = Field(default=UNSET, alias="deviceFilter")
    earliest: Optional[RFC3339DateTime] = UNSET
    latest: Optional[RFC3339DateTime] = UNSET


class ESimprovhistoryRequestDict(TypedDict):
    account_name: NotRequired[str]
    device_filter: NotRequired[list[DeviceId2 | DeviceId2Dict]]
    earliest: NotRequired[RFC3339DateTime]
    latest: NotRequired[RFC3339DateTime]
