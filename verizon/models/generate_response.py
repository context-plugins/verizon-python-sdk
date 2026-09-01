from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .generate_response_item import GenerateResponseItem, GenerateResponseItemDict


class GenerateResponse(SdkBaseModel):
    items: Optional[list[GenerateResponseItem]] = UNSET


class GenerateResponseDict(TypedDict):
    items: NotRequired[list[GenerateResponseItem | GenerateResponseItemDict]]
