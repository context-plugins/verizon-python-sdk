from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .e_simdevice_list import ESimdeviceList, ESimdeviceListDict


class ESimprofileRequest2(SdkBaseModel):
    devices: Optional[list[ESimdeviceList]] = UNSET
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")


class ESimprofileRequest2Dict(TypedDict):
    devices: NotRequired[list[ESimdeviceList | ESimdeviceListDict]]
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
    mdn_zip_code: NotRequired[str]
