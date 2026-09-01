from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .smsmessage import Smsmessage, SmsmessageDict


class SmsmessagesQueryResult(SdkBaseModel):
    """Response to SMS messages sent by all M2M devices associated with a billing account."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved."""

    messages: Optional[list[Smsmessage]] = UNSET
    """An array of up to 100 SMS messages that were sent by devices in the account."""


class SmsmessagesQueryResultDict(TypedDict):
    has_more_data: NotRequired[bool]
    messages: NotRequired[list[Smsmessage | SmsmessageDict]]
