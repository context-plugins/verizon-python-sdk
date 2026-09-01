from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_idarray import DeviceIdarray, DeviceIdarrayDict


class FallBack(SdkBaseModel):
    devices: Optional[list[list[DeviceIdarray]]] = UNSET
    """An array containing the ``deviceId`` array."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included."""


class FallBackDict(TypedDict):
    devices: NotRequired[list[list[DeviceIdarray | DeviceIdarrayDict]]]
    account_name: NotRequired[str]
