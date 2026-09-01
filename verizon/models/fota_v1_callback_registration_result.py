from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV1CallbackRegistrationResult(SdkBaseModel):
    """Registered callback account name and service name."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the billing account for which callback messages will be sent."""

    service_name: Optional[str] = Field(default=UNSET, alias="serviceName")
    """The name of the callback service, which identifies the type and format of messages that will be sent to the
    registered URL. This will be 'Fota' for the Software Management Services callback."""


class FotaV1CallbackRegistrationResultDict(TypedDict):
    account_name: NotRequired[str]
    service_name: NotRequired[str]
