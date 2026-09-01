from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GenerateResponseItemCredential(SdkBaseModel):
    username: Optional[str] = UNSET
    password: Optional[str] = UNSET


class GenerateResponseItemCredentialDict(TypedDict):
    username: NotRequired[str]
    password: NotRequired[str]
