from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict


class AccountLead(SdkBaseModel):
    """A successful response returns an array of lead objects."""

    address: Optional[Address] = UNSET
    """The customer address for the line's primary place of use, for line usage taxation."""

    lead_id: Optional[str] = Field(default=UNSET, alias="leadId")
    """Unique number for each lead. Use this value in the leadId parameter when activating devices to credit the
    activations to the lead."""

    lead_state: Optional[str] = Field(default=UNSET, alias="leadState")
    """The current state of the lead, such as “Qualified” or “Closed.”"""


class AccountLeadDict(TypedDict):
    address: NotRequired[Address | AddressDict]
    lead_id: NotRequired[str]
    lead_state: NotRequired[str]
