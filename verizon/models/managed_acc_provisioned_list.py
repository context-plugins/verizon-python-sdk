from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ManagedAccProvisionedList(SdkBaseModel):
    id: Optional[str] = UNSET
    """Account name"""

    txid: Optional[str] = UNSET
    """Transaction identifier"""


class ManagedAccProvisionedListDict(TypedDict):
    id: NotRequired[str]
    txid: NotRequired[str]
