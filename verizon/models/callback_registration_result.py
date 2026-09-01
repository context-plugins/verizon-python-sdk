from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.callback_service_name import CallbackServiceNameOrStr


class CallbackRegistrationResult(SdkBaseModel):
    account: Optional[str] = UNSET
    """The name of the account that registered the callback URL."""

    name: Optional[CallbackServiceNameOrStr] = UNSET
    """The name of the callback service."""


class CallbackRegistrationResultDict(TypedDict):
    account: NotRequired[str]
    name: NotRequired[CallbackServiceNameOrStr]
