from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class UsageHistory(SdkBaseModel):
    bytes_used: Optional[int] = Field(default=UNSET, alias="bytesUsed")
    serviceplan: Optional[str] = UNSET
    sms_used: Optional[int] = Field(default=UNSET, alias="smsUsed")
    mo_sms: Optional[int] = Field(default=UNSET, alias="moSMS")
    mt_sms: Optional[int] = Field(default=UNSET, alias="mtSMS")
    source: Optional[str] = UNSET
    event_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="eventDateTime")


class UsageHistoryDict(TypedDict):
    bytes_used: NotRequired[int]
    serviceplan: NotRequired[str]
    sms_used: NotRequired[int]
    mo_sms: NotRequired[int]
    mt_sms: NotRequired[int]
    source: NotRequired[str]
    event_date_time: NotRequired[RFC3339DateTime]
