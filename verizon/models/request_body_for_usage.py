from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .ready_sim_device_id import ReadySimDeviceId, ReadySimDeviceIdDict


class RequestBodyForUsage(SdkBaseModel):
    account_id: Optional[str] = Field(default=UNSET, alias="accountId")
    device_id: Optional[list[ReadySimDeviceId]] = Field(default=UNSET, alias="deviceId")
    start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startTime")
    end_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endTime")


class RequestBodyForUsageDict(TypedDict):
    account_id: NotRequired[str]
    device_id: NotRequired[list[ReadySimDeviceId | ReadySimDeviceIdDict]]
    start_time: NotRequired[RFC3339DateTime]
    end_time: NotRequired[RFC3339DateTime]
