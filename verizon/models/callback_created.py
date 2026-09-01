from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallbackCreated(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """The numeric name of the account and must include leading zeroes."""

    name: str
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL."""

    url: Optional[str] = UNSET
    """The address of the callback listening service where the ThingSpace Platform will send callback messages for the
    service type."""


class CallbackCreatedDict(TypedDict):
    account_name: str
    name: str
    url: NotRequired[str]
