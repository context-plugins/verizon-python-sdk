from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExtendedAttributes(SdkBaseModel):
    """Additional properties associated with data."""

    key: Optional[str] = UNSET
    value: Optional[str] = UNSET


class ExtendedAttributesDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]
