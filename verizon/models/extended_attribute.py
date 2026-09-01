from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExtendedAttribute(SdkBaseModel):
    key: Optional[str] = UNSET
    """The key indicates if the SMS message was to the device (MtSms) or from the device (MoSms)"""

    value: Optional[str] = UNSET
    """The number of SMS messages found"""


class ExtendedAttributeDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]
