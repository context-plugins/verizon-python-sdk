from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BillUsageRequest(SdkBaseModel):
    """Bill usage request."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    start_date: str = Field(alias="startDate")
    """Start date to search for billable usage, mm-dd-yyyy."""

    end_date: str = Field(alias="endDate")
    """End date to search for billable usage, mm-dd-yyyy."""

    usage_for_all_accounts: Optional[bool] = Field(default=UNSET, alias="usageForAllAccounts")
    """Request usage for single or multiple accounts."""


class BillUsageRequestDict(TypedDict):
    account_name: str
    start_date: str
    end_date: str
    usage_for_all_accounts: NotRequired[bool]
