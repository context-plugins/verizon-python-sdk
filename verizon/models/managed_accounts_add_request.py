from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class ManagedAccountsAddRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """Account identifier"""

    service_name: ServiceNameOrStr = Field(alias="serviceName")
    """Service name"""

    type_: str = Field(alias="type")
    """SKU name"""

    managed_acc_list: list[str] = Field(alias="managedAccList")
    """managed account list"""


class ManagedAccountsAddRequestDict(TypedDict):
    account_name: str
    service_name: ServiceNameOrStr
    type_: str
    managed_acc_list: list[str]
