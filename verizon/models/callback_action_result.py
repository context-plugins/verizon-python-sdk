from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallbackActionResult(SdkBaseModel):
    """Response to a callback action."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the billing account."""

    service_name: Optional[str] = Field(default=UNSET, alias="serviceName")
    """The name of the callback service that was registered/deregistered."""


class CallbackActionResultDict(TypedDict):
    account_name: NotRequired[str]
    service_name: NotRequired[str]
