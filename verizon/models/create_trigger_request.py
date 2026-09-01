from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .anomaly_trigger_request import AnomalyTriggerRequest, AnomalyTriggerRequestDict
from .data_trigger_request import DataTriggerRequest, DataTriggerRequestDict
from .session_trigger_request import SessionTriggerRequest, SessionTriggerRequestDict
from .smstrigger_request import SmstriggerRequest, SmstriggerRequestDict


class CreateTriggerRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    anomaly_trigger_request: Optional[AnomalyTriggerRequest] = Field(default=UNSET, alias="anomalyTriggerRequest")
    """The details of the UsageAnomaly trigger."""

    data_trigger_request: Optional[DataTriggerRequest] = Field(default=UNSET, alias="dataTriggerRequest")
    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    name: Optional[str] = UNSET
    session_trigger_request: Optional[SessionTriggerRequest] = Field(default=UNSET, alias="sessionTriggerRequest")
    sms_trigger_request: Optional[SmstriggerRequest] = Field(default=UNSET, alias="smsTriggerRequest")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    trigger_cycle: Optional[str] = Field(default=UNSET, alias="triggerCycle")


class CreateTriggerRequestDict(TypedDict):
    account_name: NotRequired[str]
    anomaly_trigger_request: NotRequired[AnomalyTriggerRequest | AnomalyTriggerRequestDict]
    data_trigger_request: NotRequired[DataTriggerRequest | DataTriggerRequestDict]
    group_name: NotRequired[str]
    name: NotRequired[str]
    session_trigger_request: NotRequired[SessionTriggerRequest | SessionTriggerRequestDict]
    sms_trigger_request: NotRequired[SmstriggerRequest | SmstriggerRequestDict]
    trigger_category: NotRequired[str]
    trigger_cycle: NotRequired[str]
