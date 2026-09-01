from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GbiAddress5(SdkBaseModel):
    address_line1: Optional[str] = Field(default=UNSET, alias="addressLine1")
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    zip: Optional[str] = UNSET
    zip_4: Optional[str] = Field(default=UNSET, alias="zip+4")
    phone: Optional[str] = UNSET
    phone_type: Optional[str] = Field(default=UNSET, alias="phoneType")
    email_address: Optional[str] = Field(default=UNSET, alias="emailAddress")


class GbiAddress5Dict(TypedDict):
    address_line1: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    zip_4: NotRequired[str]
    phone: NotRequired[str]
    phone_type: NotRequired[str]
    email_address: NotRequired[str]
