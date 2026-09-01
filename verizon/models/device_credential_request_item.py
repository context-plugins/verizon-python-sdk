from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceCredentialRequestItem(SdkBaseModel):
    imei: str
    """15-digit alphanumeric identifier"""


class DeviceCredentialRequestItemDict(TypedDict):
    imei: str
