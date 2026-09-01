from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ManagedAccAddedList(SdkBaseModel):
    id: Optional[str] = UNSET
    """Account name"""

    txid: Optional[str] = UNSET
    """Transaction identifier"""


class ManagedAccAddedListDict(TypedDict):
    id: NotRequired[str]
    txid: NotRequired[str]
