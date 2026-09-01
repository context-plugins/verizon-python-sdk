from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AllowanceThreshold(SdkBaseModel):
    percentage50: Optional[bool] = UNSET
    percentage75: Optional[bool] = UNSET
    percentage90: Optional[bool] = UNSET
    percentage100: Optional[bool] = UNSET


class AllowanceThresholdDict(TypedDict):
    percentage50: NotRequired[bool]
    percentage75: NotRequired[bool]
    percentage90: NotRequired[bool]
    percentage100: NotRequired[bool]
