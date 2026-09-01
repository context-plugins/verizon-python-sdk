from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoHealthScoreMetric(SdkBaseModel):
    metrictype: Optional[str] = UNSET
    """The type of measurement and can be overallscore, networkscore, gatewayscore, sensorscore, networkstatus,
    averagesignalstrength or networkavailabilitylast30"""

    metricvalue: Optional[str] = UNSET
    """the value of the ``metrictype`` as a percentage"""


class DtoHealthScoreMetricDict(TypedDict):
    metrictype: NotRequired[str]
    metricvalue: NotRequired[str]
