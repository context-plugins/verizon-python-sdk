from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.request_status import RequestStatusOrStr


class AsynchronousRequestResult(SdkBaseModel):
    """A successful request returns the request ID and the current status."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """The unique ID of the asynchronous request."""

    status: Optional[RequestStatusOrStr] = UNSET
    """The current status of the callback response."""


class AsynchronousRequestResultDict(TypedDict):
    request_id: NotRequired[str]
    status: NotRequired[RequestStatusOrStr]
