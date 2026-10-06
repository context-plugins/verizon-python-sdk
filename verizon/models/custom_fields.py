from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CustomFields(SdkBaseModel):
    """Custom data that can be included using key-value pairs."""

    key: str
    """The key for an extended attribute."""

    value: str
    """The value of an extended attribute."""


class CustomFieldsDict(TypedDict):
    key: str
    value: str
