from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V3TimeWindow(SdkBaseModel):
    """Time window."""

    start_time: int = Field(alias="startTime")
    """Start hour in range [0..23], current hour >= startTime."""

    end_time: int = Field(alias="endTime")
    """End hour in range [1..24], current hour < endTime."""


class V3TimeWindowDict(TypedDict):
    start_time: int
    end_time: int
