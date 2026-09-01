from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TextPhraseItemContent(SdkBaseModel):
    """An item object wrapping a text phrase value."""

    text: str
    """Text phrase provides very short sections of text interspersed between the ITIS codes to create phrases. In
    general, this is used for expressing proper nouns, such as street names reflecting local expressions that do not
    appear in the ITIS tables."""


class TextPhraseItemContentDict(TypedDict):
    text: str
