from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .text_item_content import TextItemContent, TextItemContentDict


class TextItemWrapper(SdkBaseModel):
    """A wrapper carrying a text item."""

    item: TextItemContent
    """An item object wrapping a text value."""


class TextItemWrapperDict(TypedDict):
    item: TextItemContent | TextItemContentDict
