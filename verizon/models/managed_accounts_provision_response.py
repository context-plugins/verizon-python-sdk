from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class ManagedAccountsProvisionResponse(SdkBaseModel):
    txid: Optional[str] = UNSET
    """Transaction identifier"""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier"""

    paccount_name: Optional[str] = Field(default=UNSET, alias="paccountName")
    """Primary Account identifier"""

    service_name: Optional[ServiceNameOrStr] = Field(default=UNSET, alias="serviceName")
    """Service name"""

    status: Optional[str] = UNSET
    """Provision status. Success or Fail"""

    reason: Optional[str] = UNSET
    """Detailed reason"""


class ManagedAccountsProvisionResponseDict(TypedDict):
    txid: NotRequired[str]
    account_name: NotRequired[str]
    paccount_name: NotRequired[str]
    service_name: NotRequired[ServiceNameOrStr]
    status: NotRequired[str]
    reason: NotRequired[str]
