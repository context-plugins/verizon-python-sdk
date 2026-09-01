from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .attribute_setting import AttributeSetting, AttributeSettingDict
from .device import Device, DeviceDict


class DiagnosticObservationSetting(SdkBaseModel):
    """Diagnostic observation settings and attributes for a device."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the billing account for which callback messages will be sent. Format: "##########-#####"."""

    device: Optional[Device] = UNSET
    """Identifies a particular IoT device."""

    attributes: Optional[list[AttributeSetting]] = UNSET
    """Streaming RF parameters for which you want to retrieve diagnostic settings."""


class DiagnosticObservationSettingDict(TypedDict):
    account_name: NotRequired[str]
    device: NotRequired[Device | DeviceDict]
    attributes: NotRequired[list[AttributeSetting | AttributeSettingDict]]
