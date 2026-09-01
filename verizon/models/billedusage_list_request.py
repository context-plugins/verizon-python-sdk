from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_cycle import BillingCycle, BillingCycleDict
from .device_list import DeviceList, DeviceListDict
from .labels_list import LabelsList, LabelsListDict


class BilledusageListRequest(SdkBaseModel):
    """Information required to associate a usage segmentation label with a device to retrieve billing."""

    account_name: str = Field(alias="accountName")
    labels: Optional[LabelsList] = UNSET
    device_ids: Optional[list[DeviceList]] = Field(default=UNSET, alias="deviceIds")
    billing_cycle: Optional[BillingCycle] = Field(default=UNSET, alias="billingCycle")


class BilledusageListRequestDict(TypedDict):
    account_name: str
    labels: NotRequired[LabelsList | LabelsListDict]
    device_ids: NotRequired[list[DeviceList | DeviceListDict]]
    billing_cycle: NotRequired[BillingCycle | BillingCycleDict]
