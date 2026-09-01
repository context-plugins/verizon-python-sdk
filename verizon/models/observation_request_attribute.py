from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.attribute_identifier import AttributeIdentifierOrStr


class ObservationRequestAttribute(SdkBaseModel):
    """Streaming RF parameter that you want to observe."""

    name: Optional[AttributeIdentifierOrStr] = UNSET
    """Attribute identifier."""


class ObservationRequestAttributeDict(TypedDict):
    name: NotRequired[AttributeIdentifierOrStr]
