from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SecuritySuccessResult(SdkBaseModel):
    """Success response."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """A unique string that associates the request with the results that are sent via a callback message.The ThingSpace
    Platform sends a separate callback message for each device that matches the request criteria, indicating whether the
    operation succeeded for that device and containing any requested information. All callback messages will have the
    same requestId."""


class SecuritySuccessResultDict(TypedDict):
    request_id: NotRequired[str]
