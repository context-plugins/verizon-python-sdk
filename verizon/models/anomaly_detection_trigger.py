from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AnomalyDetectionTrigger(SdkBaseModel):
    """Trigger for anomaly detection."""

    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """Trigger ID to identify the request in a callback."""


class AnomalyDetectionTriggerDict(TypedDict):
    trigger_id: NotRequired[str]
