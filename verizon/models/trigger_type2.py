from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .trigger_notification import TriggerNotification, TriggerNotificationDict
from .usage_anomaly_attributes import UsageAnomalyAttributes, UsageAnomalyAttributesDict


class TriggerType2(SdkBaseModel):
    """Trigger details."""

    anomalyattributes: Optional[UsageAnomalyAttributes] = UNSET
    """The details of the UsageAnomaly trigger."""

    notification: Optional[TriggerNotification] = UNSET
    """The notification details of the trigger."""


class TriggerType2Dict(TypedDict):
    anomalyattributes: NotRequired[UsageAnomalyAttributes | UsageAnomalyAttributesDict]
    notification: NotRequired[TriggerNotification | TriggerNotificationDict]
