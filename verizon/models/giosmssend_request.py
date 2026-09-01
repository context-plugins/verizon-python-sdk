from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict
from .kv_pair import KvPair, KvPairDict


class GiosmssendRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    custom_fields: Optional[list[KvPair]] = Field(default=UNSET, alias="customFields")
    data_encoding: Optional[str] = Field(default=UNSET, alias="dataEncoding")
    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    time_to_live: Optional[str] = Field(default=UNSET, alias="timeToLive")
    """A period of time the message remains valid or an end date for the message. This value would be less than the 5
    day default."""

    device_ids: Optional[list[GiodeviceId]] = Field(default=UNSET, alias="deviceIds")
    sms_message: str = Field(alias="smsMessage")


class GiosmssendRequestDict(TypedDict):
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[KvPair | KvPairDict]]
    data_encoding: NotRequired[str]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
    time_to_live: NotRequired[str]
    device_ids: NotRequired[list[GiodeviceId | GiodeviceIdDict]]
    sms_message: str
