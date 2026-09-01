from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Cellphonenumber(SdkBaseModel):
    number: Optional[str] = UNSET
    carrier: Optional[str] = UNSET


class CellphonenumberDict(TypedDict):
    number: NotRequired[str]
    carrier: NotRequired[str]
