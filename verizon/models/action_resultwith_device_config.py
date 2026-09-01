from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .dto_device_action_set_configuration import DtoDeviceActionSetConfiguration, DtoDeviceActionSetConfigurationDict


class ActionResultwithDeviceConfig(SdkBaseModel):
    createdon: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    description: Optional[str] = UNSET
    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""

    errmsg: Optional[str] = UNSET
    """Error message"""

    fields: Optional[DtoDeviceActionSetConfiguration] = UNSET
    foreignid: Optional[str] = UNSET
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastupdated: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    state: Optional[str] = UNSET
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    transactionid: Optional[str] = UNSET
    """The system-generated UUID of the transaction"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: Optional[str] = UNSET
    """The UUID of the resource version"""


class ActionResultwithDeviceConfigDict(TypedDict):
    createdon: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    deviceid: NotRequired[str]
    errmsg: NotRequired[str]
    fields: NotRequired[DtoDeviceActionSetConfiguration | DtoDeviceActionSetConfigurationDict]
    foreignid: NotRequired[str]
    id: NotRequired[str]
    lastupdated: NotRequired[RFC3339DateTime]
    state: NotRequired[str]
    transactionid: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
