from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .text_phrase_item_content import TextPhraseItemContent, TextPhraseItemContentDict


class TextPhraseItemWrapper(SdkBaseModel):
    """A wrapper carrying a text phrase item."""

    item: TextPhraseItemContent
    """An item object wrapping a text phrase value."""


class TextPhraseItemWrapperDict(TypedDict):
    item: TextPhraseItemContent | TextPhraseItemContentDict
