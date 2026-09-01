from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CarrierInformation(SdkBaseModel):
    """Information about the carrier."""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """The carrier that will perform the activation. This parameter is only required if you have more than one
    carrier."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The service plan code that is assigned to the device."""

    state: Optional[str] = UNSET
    """The device state. Valid values include: Activate, Suspend, Deactive, Pre-active."""


class CarrierInformationDict(TypedDict):
    carrier_name: NotRequired[str]
    service_plan: NotRequired[str]
    state: NotRequired[str]
