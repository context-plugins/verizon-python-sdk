from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .anomaly_trigger_request import AnomalyTriggerRequest, AnomalyTriggerRequestDict
from .data_trigger_request import DataTriggerRequest, DataTriggerRequestDict
from .enums.cycle_type import CycleTypeOrStr
from .promo_alert_trigger_request import PromoAlertTriggerRequest, PromoAlertTriggerRequestDict
from .session_trigger_request import SessionTriggerRequest, SessionTriggerRequestDict
from .smstrigger_request import SmstriggerRequest, SmstriggerRequestDict


class UpdateTriggerRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    active: Optional[bool] = UNSET
    anomaly_trigger_request: Optional[AnomalyTriggerRequest] = Field(default=UNSET, alias="anomalyTriggerRequest")
    """The details of the UsageAnomaly trigger."""

    cycle_type: Optional[CycleTypeOrStr] = Field(default=UNSET, alias="cycleType")
    data_trigger_request: Optional[DataTriggerRequest] = Field(default=UNSET, alias="dataTriggerRequest")
    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    promo_alert_trigger_request: Optional[PromoAlertTriggerRequest] = Field(
        default=UNSET, alias="promoAlertTriggerRequest"
    )
    session_trigger_request: Optional[SessionTriggerRequest] = Field(default=UNSET, alias="sessionTriggerRequest")
    sms_trigger_request: Optional[SmstriggerRequest] = Field(default=UNSET, alias="smsTriggerRequest")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")


class UpdateTriggerRequestDict(TypedDict):
    account_name: NotRequired[str]
    active: NotRequired[bool]
    anomaly_trigger_request: NotRequired[AnomalyTriggerRequest | AnomalyTriggerRequestDict]
    cycle_type: NotRequired[CycleTypeOrStr]
    data_trigger_request: NotRequired[DataTriggerRequest | DataTriggerRequestDict]
    group_name: NotRequired[str]
    promo_alert_trigger_request: NotRequired[PromoAlertTriggerRequest | PromoAlertTriggerRequestDict]
    session_trigger_request: NotRequired[SessionTriggerRequest | SessionTriggerRequestDict]
    sms_trigger_request: NotRequired[SmstriggerRequest | SmstriggerRequestDict]
    trigger_category: NotRequired[str]
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
