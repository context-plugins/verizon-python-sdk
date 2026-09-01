from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoQueryMetricsResponse(SdkBaseModel):
    critical: Optional[int] = UNSET
    """The number of critical alerts in the queried time period"""

    major: Optional[int] = UNSET
    """The number of major alerts in the queried time period"""

    minor: Optional[int] = UNSET
    """The number of minor alerts in the queried time period"""

    noalert: Optional[int] = UNSET
    """The number of sensor reports containing no alerts in the queried time period"""

    total: Optional[int] = UNSET
    """The total number of alerts in the queried time period"""

    deltacritical: Optional[int] = UNSET
    """The change in the number of critical alerts in the queried time period"""

    deltamajor: Optional[int] = UNSET
    """The change in the number of major alerts in the queried time period"""

    deltaminor: Optional[int] = UNSET
    """The change in the number of minor alerts in the queried time period"""

    deltanoalert: Optional[int] = UNSET
    """The change in the number of sensor reports containing no alerts in the queried time period"""


class DtoQueryMetricsResponseDict(TypedDict):
    critical: NotRequired[int]
    major: NotRequired[int]
    minor: NotRequired[int]
    noalert: NotRequired[int]
    total: NotRequired[int]
    deltacritical: NotRequired[int]
    deltamajor: NotRequired[int]
    deltaminor: NotRequired[int]
    deltanoalert: NotRequired[int]
