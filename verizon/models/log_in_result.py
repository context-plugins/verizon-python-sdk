from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LogInResult(SdkBaseModel):
    """Response to initiate a Connectivity Management session and returns a VZ-M2M session token that is required in
    subsequent API requests."""

    session_token: Optional[str] = Field(default=UNSET, alias="sessionToken")
    """The identifier for the session that was created by the request. Store the sessionToken for use in the header of
    all other API requests."""


class LogInResultDict(TypedDict):
    session_token: NotRequired[str]
