from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_profile import DtoProfile, DtoProfileDict


class DtoConfigurationProfile(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    profiles: Optional[list[DtoProfile]] = UNSET


class DtoConfigurationProfileDict(TypedDict):
    accountname: NotRequired[str]
    profiles: NotRequired[list[DtoProfile | DtoProfileDict]]
