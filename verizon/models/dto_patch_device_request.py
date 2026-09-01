from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_device_resource_identifier import DtoDeviceResourceIdentifier, DtoDeviceResourceIdentifierDict
from .resource_device import ResourceDevice, ResourceDeviceDict


class DtoPatchDeviceRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    device: Optional[ResourceDevice] = UNSET
    resourceidentifier: Optional[DtoDeviceResourceIdentifier] = UNSET
    """Device identifiers, one or more are required"""


class DtoPatchDeviceRequestDict(TypedDict):
    accountname: NotRequired[str]
    device: NotRequired[ResourceDevice | ResourceDeviceDict]
    resourceidentifier: NotRequired[DtoDeviceResourceIdentifier | DtoDeviceResourceIdentifierDict]
