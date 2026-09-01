from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountConsentUpdate(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account, including leading zeros."""

    all_device_consent: Optional[int] = Field(default=UNSET, alias="allDeviceConsent")
    """The consent setting to use for all the devices in the account."""


class AccountConsentUpdateDict(TypedDict):
    account_name: NotRequired[str]
    all_device_consent: NotRequired[int]
