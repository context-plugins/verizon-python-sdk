from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DailyUsageItem(SdkBaseModel):
    """Contains only dates when device had sessions."""

    start_time: Optional[str] = Field(default=UNSET, alias="startTime")
    """Start date of session. ISO 8601 format."""

    end_time: Optional[str] = Field(default=UNSET, alias="endTime")
    """End date of session. ISO 8601 format."""

    num_bytes: Optional[int] = Field(default=UNSET, alias="numBytes")
    """Amount of data transferred, measured in Bytes."""


class DailyUsageItemDict(TypedDict):
    start_time: NotRequired[str]
    end_time: NotRequired[str]
    num_bytes: NotRequired[int]
