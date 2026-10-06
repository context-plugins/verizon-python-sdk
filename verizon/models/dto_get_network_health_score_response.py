from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_health_score_metric import DtoHealthScoreMetric, DtoHealthScoreMetricDict


class DtoGetNetworkHealthScoreResponse(SdkBaseModel):
    """The values measured are for the network"""

    networksummary: Optional[list[DtoHealthScoreMetric]] = UNSET
    overallsummary: Optional[list[DtoHealthScoreMetric]] = UNSET


class DtoGetNetworkHealthScoreResponseDict(TypedDict):
    networksummary: NotRequired[list[DtoHealthScoreMetricDict]]
    overallsummary: NotRequired[list[DtoHealthScoreMetricDict]]
