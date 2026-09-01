from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChangePwndeviceStateResponse(SdkBaseModel):
    """Response to change PWN device state"""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """A unique string that associates the request with the results that are sent via a callback service."""


class ChangePwndeviceStateResponseDict(TypedDict):
    request_id: NotRequired[str]
