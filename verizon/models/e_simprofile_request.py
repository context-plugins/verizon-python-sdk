from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .e_simdevice_list import ESimdeviceList, ESimdeviceListDict


class ESimprofileRequest(SdkBaseModel):
    devices: Optional[list[ESimdeviceList]] = UNSET
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")


class ESimprofileRequestDict(TypedDict):
    devices: NotRequired[list[ESimdeviceList | ESimdeviceListDict]]
    carrier_name: NotRequired[str]
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
    mdn_zip_code: NotRequired[str]
