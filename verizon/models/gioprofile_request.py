from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_list import GiodeviceList, GiodeviceListDict


class GioprofileRequest(SdkBaseModel):
    devices: list[GiodeviceList]
    account_name: str = Field(alias="accountName")
    smrs_oid: Optional[str] = Field(default=UNSET, alias="smrsOid")
    """The Subscription Manager Secure Router Object ID, used for remote SIM provisioning. SMSR securely routes the
    download and management of eSIM profiles."""

    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")


class GioprofileRequestDict(TypedDict):
    devices: list[GiodeviceList | GiodeviceListDict]
    account_name: str
    smrs_oid: NotRequired[str]
    mdn_zip_code: NotRequired[str]
    service_plan: NotRequired[str]
