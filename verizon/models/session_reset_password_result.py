from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SessionResetPasswordResult(SdkBaseModel):
    """Response to a new, randomly generated password for the current username."""

    new_password: Optional[str] = Field(default=UNSET, alias="newPassword")
    """The new password for the username."""


class SessionResetPasswordResultDict(TypedDict):
    new_password: NotRequired[str]
