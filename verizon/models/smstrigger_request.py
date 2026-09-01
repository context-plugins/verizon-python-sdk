from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SmstriggerRequest(SdkBaseModel):
    comparator: Optional[str] = UNSET
    sms_type: Optional[str] = Field(default=UNSET, alias="smsType")
    threshold: Optional[int] = UNSET


class SmstriggerRequestDict(TypedDict):
    comparator: NotRequired[str]
    sms_type: NotRequired[str]
    threshold: NotRequired[int]
