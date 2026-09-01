from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SmsoptionsSendRequest(SdkBaseModel):
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    sms_message: Optional[str] = Field(default=UNSET, alias="smsMessage")


class SmsoptionsSendRequestDict(TypedDict):
    service_plan: NotRequired[str]
    sms_message: NotRequired[str]
