from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConsentTransactionId(SdkBaseModel):
    """The transaction ID of the request that you want to cancel, from the POST /devicelocations synchronus response."""

    transaction_id: Optional[str] = Field(default=UNSET, alias="transactionId")
    status: Optional[str] = UNSET


class ConsentTransactionIdDict(TypedDict):
    transaction_id: NotRequired[str]
    status: NotRequired[str]
