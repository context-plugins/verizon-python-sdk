from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actionobject import Actionobject, ActionobjectDict


class ActionObjectCall(SdkBaseModel):
    action: Optional[Actionobject] = UNSET


class ActionObjectCallDict(TypedDict):
    action: NotRequired[Actionobject | ActionobjectDict]
