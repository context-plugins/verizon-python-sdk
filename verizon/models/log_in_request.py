from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LogInRequest(SdkBaseModel):
    """Request to initiate a Connectivity Management session and returns a VZ-M2M session token that is required in
    subsequent API requests."""

    username: str
    """The username for authentication."""

    password: str
    """The password for authentication."""


class LogInRequestDict(TypedDict):
    username: str
    password: str
