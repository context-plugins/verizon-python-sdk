from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TargetAuthenticationBodyHeaders(SdkBaseModel):
    """Authentication headers."""

    authorization: Optional[str] = Field(default=UNSET, alias="Authorization")
    """Authorization header."""

    content_type: Optional[str] = Field(default=UNSET, alias="Content-Type")
    """Content-Type header."""


class TargetAuthenticationBodyHeadersDict(TypedDict):
    authorization: NotRequired[str]
    content_type: NotRequired[str]
