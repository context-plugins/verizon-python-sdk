from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .numerical_data import NumericalData, NumericalDataDict


class HistorySearchLimitTime(SdkBaseModel):
    """The time period for which a request should retrieve data, beginning with the limitTime.startOn and proceeding
    with the limitTime.duration."""

    start_on: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startOn")
    """The starting date-time for this request."""

    duration: Optional[NumericalData] = UNSET
    """Describes value and unit of time."""


class HistorySearchLimitTimeDict(TypedDict):
    start_on: NotRequired[RFC3339DateTime]
    duration: NotRequired[NumericalData | NumericalDataDict]
