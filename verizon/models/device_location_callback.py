from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.callback_service_name import CallbackServiceNameOrStr


class DeviceLocationCallback(SdkBaseModel):
    name: CallbackServiceNameOrStr
    """The name of the callback service."""

    url: str
    """The location of your callback listener."""


class DeviceLocationCallbackDict(TypedDict):
    name: CallbackServiceNameOrStr
    url: str
