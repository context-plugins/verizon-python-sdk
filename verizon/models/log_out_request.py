from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LogOutRequest(SdkBaseModel):
    """Request to end a Connectivity Management session."""

    session_token: Optional[str] = Field(default=UNSET, alias="sessionToken")
    """The session token is returned to confirm that it was invalidated."""


class LogOutRequestDict(TypedDict):
    session_token: NotRequired[str]
