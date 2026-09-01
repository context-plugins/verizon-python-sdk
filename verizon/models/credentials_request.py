from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_credential_request_item import DeviceCredentialRequestItem, DeviceCredentialRequestItemDict


class CredentialsRequest(SdkBaseModel):
    ecpd: str = Field(alias="ECPD")
    """Enterprise Customer Profile ID"""

    account_number: str = Field(alias="accountNumber")
    """Billing Account Number"""

    items: list[DeviceCredentialRequestItem]
    """List of devices (1-50 items)"""


class CredentialsRequestDict(TypedDict):
    ecpd: str
    account_number: str
    items: list[DeviceCredentialRequestItem | DeviceCredentialRequestItemDict]
