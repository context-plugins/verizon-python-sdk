from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectivityManagementCallback(SdkBaseModel):
    """Includes callback listeners that were registered through the Connectivity Management API."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the billing account for which callback messages will be sent."""

    password: Optional[str] = UNSET
    """The password defined when a URL was registered for the callback service, or an empty string if no password was
    defined."""

    service_name: Optional[str] = Field(default=UNSET, alias="serviceName")
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL."""

    url: Optional[str] = UNSET
    """The address of the callback listening service where the ThingSpace Platform will send callback messages for the
    service type."""

    username: Optional[str] = UNSET
    """The username defined when a URL was registered for the callback service, or an empty string if no username was
    defined."""


class ConnectivityManagementCallbackDict(TypedDict):
    account_name: NotRequired[str]
    password: NotRequired[str]
    service_name: NotRequired[str]
    url: NotRequired[str]
    username: NotRequired[str]
