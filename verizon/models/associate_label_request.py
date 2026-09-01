from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_labels import AccountLabels, AccountLabelsDict


class AssociateLabelRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """The name of a billing account. An account name is usually numeric, and must include any leading zeros."""

    labels: AccountLabels
    """Maximum of 2,000 objects are allowed in the array."""


class AssociateLabelRequestDict(TypedDict):
    account_name: str
    labels: AccountLabels | AccountLabelsDict
