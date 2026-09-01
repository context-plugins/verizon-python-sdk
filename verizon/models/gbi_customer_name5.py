from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GbiCustomerName5(SdkBaseModel):
    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    middle_name: Optional[str] = Field(default=UNSET, alias="middleName")
    title: Optional[str] = UNSET
    suffex: Optional[str] = UNSET


class GbiCustomerName5Dict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    middle_name: NotRequired[str]
    title: NotRequired[str]
    suffex: NotRequired[str]
