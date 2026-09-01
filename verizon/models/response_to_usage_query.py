from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ready_sim_device_id import ReadySimDeviceId, ReadySimDeviceIdDict
from .usage_history import UsageHistory, UsageHistoryDict


class ResponseToUsageQuery(SdkBaseModel):
    hasmoredata: Optional[bool] = UNSET
    device_id: Optional[ReadySimDeviceId] = Field(default=UNSET, alias="deviceId")
    usage_history: Optional[list[UsageHistory]] = Field(default=UNSET, alias="usageHistory")


class ResponseToUsageQueryDict(TypedDict):
    hasmoredata: NotRequired[bool]
    device_id: NotRequired[ReadySimDeviceId | ReadySimDeviceIdDict]
    usage_history: NotRequired[list[UsageHistory | UsageHistoryDict]]
