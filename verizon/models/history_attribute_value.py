from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.attribute_identifier import AttributeIdentifierOrStr


class HistoryAttributeValue(SdkBaseModel):
    """Streaming RF parameter for which you want to retrieve history data."""

    name: Optional[AttributeIdentifierOrStr] = UNSET
    """Attribute identifier."""

    value: Optional[str] = UNSET
    """Attribute value."""

    created_on: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdOn")
    """Date and time the request was created."""


class HistoryAttributeValueDict(TypedDict):
    name: NotRequired[AttributeIdentifierOrStr]
    value: NotRequired[str]
    created_on: NotRequired[RFC3339DateTime]
