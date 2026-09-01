from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class ManagedAccountCancelResponse(SdkBaseModel):
    txid: str
    """Transaction identifier"""

    account_name: str = Field(alias="accountName")
    """Managed account identifier"""

    paccount_name: str = Field(alias="paccountName")
    """Primary account identifier"""

    service_name: ServiceNameOrStr = Field(alias="serviceName")
    """Service name"""

    status: str
    """Deactivate/cancel status, Success or Fail"""

    reason: str
    """Detailed reason"""


class ManagedAccountCancelResponseDict(TypedDict):
    txid: str
    account_name: str
    paccount_name: str
    service_name: ServiceNameOrStr
    status: str
    reason: str
