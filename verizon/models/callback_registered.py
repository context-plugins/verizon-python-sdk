from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CallbackRegistered(SdkBaseModel):
    """Callback listener is Registered."""

    account_name: str = Field(alias="accountName")
    """The numeric name of the account and must include leading zeroes."""

    name: str
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL."""


class CallbackRegisteredDict(TypedDict):
    account_name: str
    name: str
