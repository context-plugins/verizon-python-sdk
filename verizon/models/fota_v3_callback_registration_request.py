from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV3CallbackRegistrationRequest(SdkBaseModel):
    """Callback URL where the listening service is running."""

    url: Optional[str] = UNSET
    """Callback URL for an subscribed service."""


class FotaV3CallbackRegistrationRequestDict(TypedDict):
    url: NotRequired[str]
