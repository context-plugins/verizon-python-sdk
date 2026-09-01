from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV2CallbackRegistrationResult(SdkBaseModel):
    """Callback listener URL."""

    url: Optional[str] = UNSET
    """Callback URL."""


class FotaV2CallbackRegistrationResultDict(TypedDict):
    url: NotRequired[str]
