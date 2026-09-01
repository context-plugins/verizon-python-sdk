from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .license_device_list import LicenseDeviceList, LicenseDeviceListDict


class AssignLicenseRequest(SdkBaseModel):
    """Request to assign license."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account.This parameter is required only if the UWS account used for the current API session
    has access to multiple accounts. An account name is usually numeric, and must include any leading zeros."""

    devices: Optional[list[LicenseDeviceList]] = UNSET
    """A list of 4G devices."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU). Valid skuNumbers for license types: “SIMSec-IoT-Lt”. (Lifetime) Once a license is
    assigned to a SIM, the SIM-Secure feature is enabled for the life of the SIM.“TS-BUNDLE-KTO-SIMSEC-MRC”. (Bundle)
    The SIM-Secure Flex license can be assigned to or removed from a SIM at any time. This SKU is bundled with other
    ThingSpace Services.“SIMSec-IoT”. (Flex) The SIM-Secure Flex license can be assigned to or removed from a SIM at any
    time. This SKU is purchased a la carte."""


class AssignLicenseRequestDict(TypedDict):
    account_name: NotRequired[str]
    devices: NotRequired[list[LicenseDeviceList | LicenseDeviceListDict]]
    sku_number: NotRequired[str]
