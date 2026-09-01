from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_lead import AccountLead, AccountLeadDict


class AccountLeadsResult(SdkBaseModel):
    """Returns information for all leads associated with an account."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False if no more leads.True if there is more data to be retrieved."""

    leads: Optional[list[AccountLead]] = UNSET
    """The leads associated with an account."""


class AccountLeadsResultDict(TypedDict):
    has_more_data: NotRequired[bool]
    leads: NotRequired[list[AccountLead | AccountLeadDict]]
