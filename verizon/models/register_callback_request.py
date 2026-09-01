from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RegisterCallbackRequest(SdkBaseModel):
    """Request to register a callback."""

    name: str
    """The name of the callback service that you want to subscribe to."""

    url: str
    """The address on your server where you have enabled a listening service for callback messages."""

    username: Optional[str] = UNSET
    """The user name that the M2M Platform should return in the callback messages."""

    password: Optional[str] = UNSET
    """The password that the M2M Platform should return in the callback messages."""


class RegisterCallbackRequestDict(TypedDict):
    name: str
    url: str
    username: NotRequired[str]
    password: NotRequired[str]
