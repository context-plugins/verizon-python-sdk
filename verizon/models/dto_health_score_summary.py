from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_health_score_metric import DtoHealthScoreMetric, DtoHealthScoreMetricDict


class DtoHealthScoreSummary(SdkBaseModel):
    """The values measured are for sensors and gateways"""

    overallsummary: Optional[list[DtoHealthScoreMetric]] = UNSET


class DtoHealthScoreSummaryDict(TypedDict):
    overallsummary: NotRequired[list[DtoHealthScoreMetric | DtoHealthScoreMetricDict]]
