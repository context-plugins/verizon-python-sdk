from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV2CallbackRegistrationRequest(SdkBaseModel):
    """Callback URL registration."""

    url: Optional[str] = UNSET
    """Callback URL for an subscribed service."""


class FotaV2CallbackRegistrationRequestDict(TypedDict):
    url: NotRequired[str]
