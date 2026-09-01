from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_filter import DtoFilter, DtoFilterDict


class DtoListDeviceExperienceHistoryRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    filter: Optional[DtoFilter] = UNSET


class DtoListDeviceExperienceHistoryRequestDict(TypedDict):
    accountname: NotRequired[str]
    filter: NotRequired[DtoFilter | DtoFilterDict]
