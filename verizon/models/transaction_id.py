from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionId(SdkBaseModel):
    """The transaction ID of the request that you want to cancel, from the POST /devicelocations synchronus response."""

    txid: Optional[str] = UNSET


class TransactionIdDict(TypedDict):
    txid: NotRequired[str]
