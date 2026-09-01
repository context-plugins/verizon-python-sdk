from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_device_resource_identifier import DtoDeviceResourceIdentifier, DtoDeviceResourceIdentifierDict
from .dto_filter import DtoFilter, DtoFilterDict


class DtoListDevicesRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    filter: Optional[DtoFilter] = UNSET
    resourceidentifier: Optional[DtoDeviceResourceIdentifier] = UNSET
    """Device identifiers, one or more are required"""


class DtoListDevicesRequestDict(TypedDict):
    accountname: NotRequired[str]
    filter: NotRequired[DtoFilter | DtoFilterDict]
    resourceidentifier: NotRequired[DtoDeviceResourceIdentifier | DtoDeviceResourceIdentifierDict]
