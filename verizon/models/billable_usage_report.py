from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service_usage import ServiceUsage, ServiceUsageDict


class BillableUsageReport(SdkBaseModel):
    """Bill usage report."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier."""

    usage_for_all_accounts: Optional[bool] = Field(default=UNSET, alias="usageForAllAccounts")
    """The usage is for a single or multiple accounts."""

    sku_name: Optional[str] = Field(default=UNSET, alias="skuName")
    """SKU Name of the service subscription."""

    transactions_allowed: Optional[str] = Field(default=UNSET, alias="transactionsAllowed")
    """The number of location requests included with the subscription type."""

    total_transaction_count: Optional[str] = Field(default=UNSET, alias="totalTransactionCount")
    """The total number of billable device location requests during the reporting period from all included accounts."""

    primary_account: Optional[ServiceUsage] = Field(default=UNSET, alias="PrimaryAccount")
    managed_accounts: Optional[list[ServiceUsage]] = Field(default=UNSET, alias="ManagedAccounts")
    """Zero or more managed accounts."""


class BillableUsageReportDict(TypedDict):
    account_name: NotRequired[str]
    usage_for_all_accounts: NotRequired[bool]
    sku_name: NotRequired[str]
    transactions_allowed: NotRequired[str]
    total_transaction_count: NotRequired[str]
    primary_account: NotRequired[ServiceUsage | ServiceUsageDict]
    managed_accounts: NotRequired[list[ServiceUsage | ServiceUsageDict]]
