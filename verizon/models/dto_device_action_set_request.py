from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_device_action_set_configuration import DtoDeviceActionSetConfiguration, DtoDeviceActionSetConfigurationDict
from .dto_device_resource_identifier import DtoDeviceResourceIdentifier, DtoDeviceResourceIdentifierDict


class DtoDeviceActionSetRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    configuration: Optional[DtoDeviceActionSetConfiguration] = UNSET
    resourceidentifier: Optional[DtoDeviceResourceIdentifier] = UNSET
    """Device identifiers, one or more are required"""


class DtoDeviceActionSetRequestDict(TypedDict):
    accountname: NotRequired[str]
    configuration: NotRequired[DtoDeviceActionSetConfiguration | DtoDeviceActionSetConfigurationDict]
    resourceidentifier: NotRequired[DtoDeviceResourceIdentifier | DtoDeviceResourceIdentifierDict]
