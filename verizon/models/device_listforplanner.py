from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .device_idforplanner import DeviceIdforplanner, DeviceIdforplannerDict
from .private_network_apns import PrivateNetworkApns, PrivateNetworkApnsDict


class DeviceListforplanner(SdkBaseModel):
    device_ids: OptionalNullable[list[DeviceIdforplanner]] = Field(default=UNSET, alias="deviceIds")
    private_network_apns: OptionalNullable[list[PrivateNetworkApns]] = Field(default=UNSET, alias="privateNetworkApns")
    ip_address: OptionalNullable[str] = Field(default=UNSET, alias="ipAddress")
    """A IPv4 address"""

    activation_code: OptionalNullable[str] = Field(default=UNSET, alias="activationCode")
    """The activation code value."""


class DeviceListforplannerDict(TypedDict):
    device_ids: NotRequired[list[DeviceIdforplannerDict] | None]
    private_network_apns: NotRequired[list[PrivateNetworkApnsDict] | None]
    ip_address: NotRequired[str | None]
    activation_code: NotRequired[str | None]
