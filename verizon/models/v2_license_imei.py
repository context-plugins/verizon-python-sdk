from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V2LicenseImei(SdkBaseModel):
    """IMEIs of the devices to assign or remove licenses."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account name."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class V2LicenseImeiDict(TypedDict):
    account_name: NotRequired[str]
    device_list: list[str]
