from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerName(SdkBaseModel):
    """The customer name to be used for line usage taxation."""

    title: Optional[str] = UNSET
    """An optional title for the customer, such as “Mr.” or “Dr.”"""

    first_name: str = Field(alias="firstName")
    """The customer's first name."""

    middle_name: Optional[str] = Field(default=UNSET, alias="middleName")
    """The customer's middle name."""

    last_name: str = Field(alias="lastName")
    """The customer's last name."""

    suffix: Optional[str] = UNSET
    """An optional suffix for the customer name, such as “Jr.” or “III.”"""


class CustomerNameDict(TypedDict):
    title: NotRequired[str]
    first_name: str
    middle_name: NotRequired[str]
    last_name: str
    suffix: NotRequired[str]
