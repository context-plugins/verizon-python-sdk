from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .daily_usage_history import DailyUsageHistory, DailyUsageHistoryDict
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class DailyUsageResponse(SdkBaseModel):
    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """A flag set to indicate if there is more than one page of data returned by the query (true) or if only one page of
    data returned (false)"""

    device_id: Optional[GiodeviceId] = Field(default=UNSET, alias="deviceId")
    usage_history: Optional[list[DailyUsageHistory]] = Field(default=UNSET, alias="usageHistory")


class DailyUsageResponseDict(TypedDict):
    has_more_data: NotRequired[bool]
    device_id: NotRequired[GiodeviceId | GiodeviceIdDict]
    usage_history: NotRequired[list[DailyUsageHistory | DailyUsageHistoryDict]]
