from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_device_config import DtoDeviceConfig, DtoDeviceConfigDict


class DtoDeviceActionSetConfiguration(SdkBaseModel):
    device_config: Optional[DtoDeviceConfig] = Field(default=UNSET, alias="deviceConfig")


class DtoDeviceActionSetConfigurationDict(TypedDict):
    device_config: NotRequired[DtoDeviceConfig | DtoDeviceConfigDict]
