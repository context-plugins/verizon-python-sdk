from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SessionResetPasswordRequest(SdkBaseModel):
    """Request to a new, randomly generated password for the current username."""

    old_password: str = Field(alias="oldPassword")
    """The current password for the username."""


class SessionResetPasswordRequestDict(TypedDict):
    old_password: str
