from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_resourceidentifier import DtoResourceidentifier, DtoResourceidentifierDict
from .rbstiltconfig import Rbstiltconfig, RbstiltconfigDict


class DtoDeviceCommand(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric account name, which must include leading zeros"""

    configuration: Optional[Rbstiltconfig] = UNSET
    resourceidentifier: Optional[DtoResourceidentifier] = UNSET


class DtoDeviceCommandDict(TypedDict):
    account_name: NotRequired[str]
    configuration: NotRequired[Rbstiltconfig | RbstiltconfigDict]
    resourceidentifier: NotRequired[DtoResourceidentifier | DtoResourceidentifierDict]
