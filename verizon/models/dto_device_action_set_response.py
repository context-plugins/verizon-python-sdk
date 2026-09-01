from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .action_resultwith_device_config import ActionResultwithDeviceConfig, ActionResultwithDeviceConfigDict


class DtoDeviceActionSetResponse(SdkBaseModel):
    actionresult: Optional[list[ActionResultwithDeviceConfig]] = UNSET


class DtoDeviceActionSetResponseDict(TypedDict):
    actionresult: NotRequired[list[ActionResultwithDeviceConfig | ActionResultwithDeviceConfigDict]]
