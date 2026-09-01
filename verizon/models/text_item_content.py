from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TextItemContent(SdkBaseModel):
    """An item object wrapping a text value."""

    text: str
    """Simple text used with ITIS codes. (Text taken from SAE J2540.)"""


class TextItemContentDict(TypedDict):
    text: str
