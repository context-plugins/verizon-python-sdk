from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HplCustomFields(SdkBaseModel):
    """User assigned custom fields to use for fitering"""

    key: Optional[str] = UNSET
    """key property"""

    value: Optional[str] = UNSET
    """value of the key property"""


class HplCustomFieldsDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]
