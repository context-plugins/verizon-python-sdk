from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WnprequestResponse(SdkBaseModel):
    """UUID of the Wireless network performance request response."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """Request id."""


class WnprequestResponseDict(TypedDict):
    request_id: NotRequired[str]
