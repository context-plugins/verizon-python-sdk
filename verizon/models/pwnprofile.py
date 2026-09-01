from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pwnprofile(SdkBaseModel):
    profile_id: Optional[str] = Field(default=UNSET, alias="profileId")
    profile_name: Optional[str] = Field(default=UNSET, alias="profileName")


class PwnprofileDict(TypedDict):
    profile_id: NotRequired[str]
    profile_name: NotRequired[str]
