from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActiveAnomalyIndicator(SdkBaseModel):
    """Whether the anomaly detection is active or not."""

    active: Optional[bool] = UNSET
    """Indicates anomaly detection is active<br />True - Anomaly detection is active.<br />False - Anomaly detection is
    not active."""


class ActiveAnomalyIndicatorDict(TypedDict):
    active: NotRequired[bool]
