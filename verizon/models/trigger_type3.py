from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .anomaly_trigger_request import AnomalyTriggerRequest, AnomalyTriggerRequestDict
from .trigger_notification import TriggerNotification, TriggerNotificationDict


class TriggerType3(SdkBaseModel):
    """Trigger details."""

    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """Trigger ID."""

    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """Trigger name."""

    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    """This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be
    relevant when this parameter is set to this value."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account name."""

    anomaly_trigger_request: Optional[AnomalyTriggerRequest] = Field(default=UNSET, alias="anomalyTriggerRequest")
    """The details of the UsageAnomaly trigger."""

    notification: Optional[TriggerNotification] = UNSET
    """The notification details of the trigger."""


class TriggerType3Dict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    trigger_category: NotRequired[str]
    account_name: NotRequired[str]
    anomaly_trigger_request: NotRequired[AnomalyTriggerRequest | AnomalyTriggerRequestDict]
    notification: NotRequired[TriggerNotification | TriggerNotificationDict]
