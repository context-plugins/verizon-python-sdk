from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomFields(SdkBaseModel):
    """Custom data that can be included using key-value pairs."""

    key: str
    """The key for an extended attribute."""

    value: Optional[str] = UNSET
    """The value of an extended attribute."""


class CustomFieldsDict(TypedDict):
    key: str
    value: NotRequired[str]
