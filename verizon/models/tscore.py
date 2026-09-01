from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Tscore(SdkBaseModel):
    profileid: Optional[str] = UNSET
    """the UUID of the profile"""

    profileversionid: Optional[str] = UNSET
    """the UUID of the profile version"""


class TscoreDict(TypedDict):
    profileid: NotRequired[str]
    profileversionid: NotRequired[str]
