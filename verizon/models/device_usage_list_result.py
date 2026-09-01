from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .usage import Usage, UsageDict


class DeviceUsageListResult(SdkBaseModel):
    """Response to return the daily network data usage of a single device during a specified time period."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved."""

    usage_history: Optional[list[Usage]] = Field(default=UNSET, alias="usageHistory")
    """Placeholder."""


class DeviceUsageListResultDict(TypedDict):
    has_more_data: NotRequired[bool]
    usage_history: NotRequired[list[Usage | UsageDict]]
