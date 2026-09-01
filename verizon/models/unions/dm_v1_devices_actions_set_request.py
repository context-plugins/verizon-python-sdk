from __future__ import annotations

from typing import TypeAlias

from ..dto_device_action_set_request import DtoDeviceActionSetRequest, DtoDeviceActionSetRequestDict
from ..dto_device_command import DtoDeviceCommand, DtoDeviceCommandDict

DmV1DevicesActionsSetRequest: TypeAlias = DtoDeviceActionSetRequest | DtoDeviceCommand

DmV1DevicesActionsSetRequestDict: TypeAlias = DtoDeviceActionSetRequestDict | DtoDeviceCommandDict
