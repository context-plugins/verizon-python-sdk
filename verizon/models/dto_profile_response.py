from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DtoProfileResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    kind: Optional[str] = UNSET
    """the user defined profile kind"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: Optional[str] = UNSET
    createdon: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    lastupdated: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    name: Optional[str] = UNSET
    """user defined profile name"""

    foreignid: Optional[str] = UNSET
    """UUID of the ECPD account the user belongs to"""

    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    modelid: Optional[str] = UNSET
    """device model id"""

    configuration: Optional[Any] = UNSET


class DtoProfileResponseDict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
    createdon: NotRequired[RFC3339DateTime]
    lastupdated: NotRequired[RFC3339DateTime]
    name: NotRequired[str]
    foreignid: NotRequired[str]
    billingaccountid: NotRequired[str]
    modelid: NotRequired[str]
    configuration: NotRequired[Any]
