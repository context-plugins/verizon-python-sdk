from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_name import CustomerName, CustomerNameDict


class Customernamequery(SdkBaseModel):
    customer_name: Optional[list[CustomerName]] = Field(default=UNSET, alias="customerName")


class CustomernamequeryDict(TypedDict):
    customer_name: NotRequired[list[CustomerName | CustomerNameDict]]
