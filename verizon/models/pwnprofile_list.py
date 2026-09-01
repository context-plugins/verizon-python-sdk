from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pwnprofile import Pwnprofile, PwnprofileDict


class PwnprofileList(SdkBaseModel):
    profiles: Optional[list[Pwnprofile]] = UNSET


class PwnprofileListDict(TypedDict):
    profiles: NotRequired[list[Pwnprofile | PwnprofileDict]]
