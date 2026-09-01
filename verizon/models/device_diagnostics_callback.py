from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DeviceDiagnosticsCallback(SdkBaseModel):
    """Callback information of an existing diagnostics subscription."""

    account_name: str = Field(alias="accountName")
    """The name of the billing account for which callback messages will be sent. Format: "##########-#####"."""

    service_name: str = Field(alias="serviceName")
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL."""

    endpoint: str
    """The URL for your web server."""

    created_on: RFC3339DateTime = Field(alias="createdOn")
    """The date and time of when this request was created."""

    http_headers: Optional[Any] = Field(default=UNSET, alias="httpHeaders")
    """Your HTTP headers."""


class DeviceDiagnosticsCallbackDict(TypedDict):
    account_name: str
    service_name: str
    endpoint: str
    created_on: RFC3339DateTime
    http_headers: NotRequired[Any]
