from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoQueryMetrics(SdkBaseModel):
    days: Optional[int] = UNSET
    """The number of days in a recent period to query"""


class DtoQueryMetricsDict(TypedDict):
    days: NotRequired[int]
