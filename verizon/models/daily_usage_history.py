from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .extended_attribute import ExtendedAttribute, ExtendedAttributeDict


class DailyUsageHistory(SdkBaseModel):
    bytes_used: Optional[str] = Field(default=UNSET, alias="bytesUsed")
    """the total data usage recorded in Bytes"""

    extended_attributes: Optional[list[ExtendedAttribute]] = Field(default=UNSET, alias="extendedAttributes")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    sms_used: Optional[str] = Field(default=UNSET, alias="smsUsed")
    """The total number of SMS messages from and to the device"""

    source: Optional[str] = UNSET
    """Where the collected data is being gathered from"""

    timestamp: Optional[str] = UNSET
    """Timestamp of when the retrieved record was completed ($datetime)"""


class DailyUsageHistoryDict(TypedDict):
    bytes_used: NotRequired[str]
    extended_attributes: NotRequired[list[ExtendedAttribute | ExtendedAttributeDict]]
    service_plan: NotRequired[str]
    sms_used: NotRequired[str]
    source: NotRequired[str]
    timestamp: NotRequired[str]
