from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1LicensesAssignedRemovedRequest(SdkBaseModel):
    """IMEIs of the devices to assign licenses to."""

    device_list: list[str] = Field(alias="deviceList")
    """The IMEIs of the devices."""


class V1LicensesAssignedRemovedRequestDict(TypedDict):
    device_list: list[str]
