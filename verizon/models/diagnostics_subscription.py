from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class DiagnosticsSubscription(SdkBaseModel):
    """Status of the diagnostic services subscription."""

    account_name: str = Field(alias="accountName")
    """Account identifier in "##########-#####". An account name is usually numeric, and must include any leading
    zeros."""

    created_on: RFC3339DateTime = Field(alias="createdOn")
    """The date and time of when the subscription was created."""

    last_updated: RFC3339DateTime = Field(alias="lastUpdated")
    """The date and time of when the subscription was last updated."""

    total_allowed: int = Field(alias="totalAllowed")
    """Number of licenses currently assigned to devices."""

    total_used: int = Field(alias="totalUsed")
    """Number of licenses currently used by the devices."""

    sku_name: str = Field(alias="skuName")
    """Name of the SKU for the account."""


class DiagnosticsSubscriptionDict(TypedDict):
    account_name: str
    created_on: RFC3339DateTime
    last_updated: RFC3339DateTime
    total_allowed: int
    total_used: int
    sku_name: str
