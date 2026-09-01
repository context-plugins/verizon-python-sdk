from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_profile import DtoProfile, DtoProfileDict
from .dto_resourceidentifier import DtoResourceidentifier, DtoResourceidentifierDict


class DtoConfigurationProfilePath(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric account name, which must include leading zeros"""

    resourceidentifier: Optional[DtoResourceidentifier] = UNSET
    profile: Optional[DtoProfile] = UNSET


class DtoConfigurationProfilePathDict(TypedDict):
    account_name: NotRequired[str]
    resourceidentifier: NotRequired[DtoResourceidentifier | DtoResourceidentifierDict]
    profile: NotRequired[DtoProfile | DtoProfileDict]
