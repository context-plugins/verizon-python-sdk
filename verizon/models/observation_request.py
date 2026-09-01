from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .numerical_data import NumericalData, NumericalDataDict
from .observation_request_attribute import ObservationRequestAttribute, ObservationRequestAttributeDict


class ObservationRequest(SdkBaseModel):
    """Used to define callbacks including the device identity, the attribute names, corresponding attribute values and
    the date/timestamp of when the observation was made."""

    account_name: str = Field(alias="accountName")
    """Account identifier in "##########-#####"."""

    devices: list[Device]
    """List of devices."""

    attributes: list[ObservationRequestAttribute]
    """Attributes are streaming RF parameters that you want to observe."""

    frequency: Optional[NumericalData] = UNSET
    """Describes value and unit of time."""

    duration: Optional[NumericalData] = UNSET
    """Describes value and unit of time."""


class ObservationRequestDict(TypedDict):
    account_name: str
    devices: list[Device | DeviceDict]
    attributes: list[ObservationRequestAttribute | ObservationRequestAttributeDict]
    frequency: NotRequired[NumericalData | NumericalDataDict]
    duration: NotRequired[NumericalData | NumericalDataDict]
