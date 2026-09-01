from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .anomaly_trigger_request import AnomalyTriggerRequest, AnomalyTriggerRequestDict
from .trigger_notification import TriggerNotification, TriggerNotificationDict


class TriggerType1(SdkBaseModel):
    """Trigger details."""

    name: Optional[str] = UNSET
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


class TriggerType1Dict(TypedDict):
    name: NotRequired[str]
    trigger_category: NotRequired[str]
    account_name: NotRequired[str]
    anomaly_trigger_request: NotRequired[AnomalyTriggerRequest | AnomalyTriggerRequestDict]
    notification: NotRequired[TriggerNotification | TriggerNotificationDict]
