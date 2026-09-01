from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giosms_message import GiosmsMessage, GiosmsMessageDict


class SmsMessagesResponse(SdkBaseModel):
    messages: Optional[list[GiosmsMessage]] = UNSET
    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")


class SmsMessagesResponseDict(TypedDict):
    messages: NotRequired[list[GiosmsMessage | GiosmsMessageDict]]
    has_more_data: NotRequired[bool]
