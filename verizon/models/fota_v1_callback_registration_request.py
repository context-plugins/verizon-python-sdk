from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV1CallbackRegistrationRequest(SdkBaseModel):
    """Callback endpoint information."""

    name: str
    """The name of the callback service that you want to subscribe to, which must be 'Fota' for Software Management
    Services callbacks."""

    url: str
    """The address on your server where you have enabled a listening service for Software Management Services callback
    messages."""

    username: Optional[str] = UNSET
    """The user name that ThingSpace should return in the callback messages."""

    password: Optional[str] = UNSET
    """The password that ThingSpace should return in the callback messages."""


class FotaV1CallbackRegistrationRequestDict(TypedDict):
    name: str
    url: str
    username: NotRequired[str]
    password: NotRequired[str]
