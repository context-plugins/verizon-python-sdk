from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload import Payload, PayloadDict


class DtoOnBoardSensorRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    payload: Optional[Payload] = UNSET


class DtoOnBoardSensorRequestDict(TypedDict):
    accountname: NotRequired[str]
    payload: NotRequired[Payload | PayloadDict]
