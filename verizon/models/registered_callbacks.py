from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RegisteredCallbacks(SdkBaseModel):
    """List of registered callback endpoints."""

    aname: Optional[str] = UNSET
    """The name of the billing account for which callback messages will be sent."""

    name: Optional[str] = UNSET
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL. This will be 'Fota' for the Software Management Services callback."""

    url: Optional[str] = UNSET
    """The address to which callback messages will be sent."""

    username: Optional[str] = UNSET
    """The user name that ThingSpace will return in the callback messages."""

    password: Optional[str] = UNSET
    """The password that ThingSpace will return in the callback messages."""


class RegisteredCallbacksDict(TypedDict):
    aname: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    username: NotRequired[str]
    password: NotRequired[str]
