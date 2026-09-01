from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .itisitem_content import ItisitemContent, ItisitemContentDict


class ItisitemWrapper(SdkBaseModel):
    """A wrapper carrying an ITIS code item."""

    item: ItisitemContent
    """An item object wrapping an ITIS code value."""


class ItisitemWrapperDict(TypedDict):
    item: ItisitemContent | ItisitemContentDict
