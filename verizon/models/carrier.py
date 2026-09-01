from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Carrier(SdkBaseModel):
    carriers: Optional[str] = UNSET
    """The list of carriers with active or available profiles"""


class CarrierDict(TypedDict):
    carriers: NotRequired[str]
