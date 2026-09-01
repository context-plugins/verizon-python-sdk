from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceUsage(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier."""

    transactions_count: Optional[str] = Field(default=UNSET, alias="transactionsCount")
    """Total requests for the account during the reporting period."""


class ServiceUsageDict(TypedDict):
    account_name: NotRequired[str]
    transactions_count: NotRequired[str]
