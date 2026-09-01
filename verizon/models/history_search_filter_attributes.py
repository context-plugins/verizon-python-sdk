from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.attribute_identifier import AttributeIdentifierOrStr


class HistorySearchFilterAttributes(SdkBaseModel):
    """Streaming RF parameters for which you want to retrieve history data."""

    name: Optional[AttributeIdentifierOrStr] = UNSET
    """Attribute identifier."""


class HistorySearchFilterAttributesDict(TypedDict):
    name: NotRequired[AttributeIdentifierOrStr]
