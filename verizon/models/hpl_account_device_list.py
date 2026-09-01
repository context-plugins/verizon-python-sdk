from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .hpl_device_id import HplDeviceId, HplDeviceIdDict


class HplAccountDeviceList(SdkBaseModel):
    """A list of device IDs"""

    device_ids: Optional[list[HplDeviceId]] = Field(default=UNSET, alias="deviceIds")


class HplAccountDeviceListDict(TypedDict):
    device_ids: NotRequired[list[HplDeviceId | HplDeviceIdDict]]
