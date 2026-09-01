from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthSubRestErrorResponseforplanner(SdkBaseModel):
    code: Optional[str] = UNSET
    message: Optional[str] = UNSET
    description: Optional[str] = UNSET


class AuthSubRestErrorResponseforplannerDict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]
    description: NotRequired[str]
