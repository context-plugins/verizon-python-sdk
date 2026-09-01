from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_device_resource_identifier import DtoDeviceResourceIdentifier, DtoDeviceResourceIdentifierDict


class DtoLastReportedTimeRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    resourceidentifier: Optional[DtoDeviceResourceIdentifier] = UNSET
    """Device identifiers, one or more are required"""


class DtoLastReportedTimeRequestDict(TypedDict):
    accountname: NotRequired[str]
    resourceidentifier: NotRequired[DtoDeviceResourceIdentifier | DtoDeviceResourceIdentifierDict]
