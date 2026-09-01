from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DistributionSchedule(SdkBaseModel):
    """The distribution schedule parameters for broadcast messages."""

    repeat_period: int = Field(alias="repeatPeriod")
    """The period (in seconds) that the message needs to be repeatedly send out."""

    duration: int
    """The amount of time (in minutes) while the messages needs to be sent out."""

    start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startTime")
    """The time (in UTC) when the message transmission should be started."""


class DistributionScheduleDict(TypedDict):
    repeat_period: int
    duration: int
    start_time: NotRequired[RFC3339DateTime]
