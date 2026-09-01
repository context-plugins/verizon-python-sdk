from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .drop_response_item import DropResponseItem, DropResponseItemDict


class DropResponse(SdkBaseModel):
    items: Optional[list[DropResponseItem]] = UNSET


class DropResponseDict(TypedDict):
    items: NotRequired[list[DropResponseItem | DropResponseItemDict]]
