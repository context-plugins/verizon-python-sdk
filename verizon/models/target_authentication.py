from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .target_authentication_body import TargetAuthenticationBody, TargetAuthenticationBodyDict


class TargetAuthentication(SdkBaseModel):
    """OAuth 2 token and refresh token for TS to stream events to Target."""

    body: Optional[TargetAuthenticationBody] = UNSET
    version: Optional[str] = UNSET


class TargetAuthenticationDict(TypedDict):
    body: NotRequired[TargetAuthenticationBody | TargetAuthenticationBodyDict]
    version: NotRequired[str]
