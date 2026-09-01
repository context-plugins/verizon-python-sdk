from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .target_authentication_body_headers import TargetAuthenticationBodyHeaders, TargetAuthenticationBodyHeadersDict
from .target_authentication_body_host import TargetAuthenticationBodyHost, TargetAuthenticationBodyHostDict


class TargetAuthenticationBody(SdkBaseModel):
    grant_type: Optional[str] = UNSET
    """Authentication grant type."""

    refresh_token: Optional[str] = UNSET
    """Refresh token."""

    scope: Optional[str] = UNSET
    """Authentication scopes."""

    headers: Optional[TargetAuthenticationBodyHeaders] = UNSET
    """Authentication headers."""

    host: Optional[TargetAuthenticationBodyHost] = UNSET
    """Host information."""


class TargetAuthenticationBodyDict(TypedDict):
    grant_type: NotRequired[str]
    refresh_token: NotRequired[str]
    scope: NotRequired[str]
    headers: NotRequired[TargetAuthenticationBodyHeaders | TargetAuthenticationBodyHeadersDict]
    host: NotRequired[TargetAuthenticationBodyHost | TargetAuthenticationBodyHostDict]
