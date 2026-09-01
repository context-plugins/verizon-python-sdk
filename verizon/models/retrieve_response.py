from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .retrieve_response_item import RetrieveResponseItem, RetrieveResponseItemDict


class RetrieveResponse(SdkBaseModel):
    items: Optional[list[RetrieveResponseItem]] = UNSET


class RetrieveResponseDict(TypedDict):
    items: NotRequired[list[RetrieveResponseItem | RetrieveResponseItemDict]]
