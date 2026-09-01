from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallbackRegistrationRequest(SdkBaseModel):
    """Specifies the callback service that is being subscribed to and the URL where the listening service is running."""

    account_name: str = Field(alias="accountName")
    """The name of the billing account for which callback messages will be sent. Format: "##########-#####"."""

    service_name: str = Field(alias="serviceName")
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL."""

    endpoint: str
    """The URL for your web server."""

    http_headers: Optional[Any] = Field(default=UNSET, alias="httpHeaders")
    """Your HTTP headers."""


class CallbackRegistrationRequestDict(TypedDict):
    account_name: str
    service_name: str
    endpoint: str
    http_headers: NotRequired[Any]
