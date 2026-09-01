from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1ListOfLicensesToRemoveRequest(SdkBaseModel):
    """List of devices to removes."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Set to 'append' to append the devices in the current request to the existing list. If there is no existing list
    then it will be created with only these devices. Leave this parameter out when you want to replace the existing list
    with the devices in the current request."""

    device_list: list[str] = Field(alias="deviceList")
    """The IMEIs of the devices."""


class V1ListOfLicensesToRemoveRequestDict(TypedDict):
    type_: NotRequired[str]
    device_list: list[str]
