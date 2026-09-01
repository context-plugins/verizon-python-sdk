from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class ManagedAccountCancelRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """Managed account identifier"""

    paccount_name: str = Field(alias="paccountName")
    """Primary Account identifier"""

    service_name: ServiceNameOrStr = Field(alias="serviceName")
    """Service name"""

    type_: str = Field(alias="type")
    """SKU name"""

    txid: str
    """Transaction identifier returned by provision request"""


class ManagedAccountCancelRequestDict(TypedDict):
    account_name: str
    paccount_name: str
    service_name: ServiceNameOrStr
    type_: str
    txid: str
