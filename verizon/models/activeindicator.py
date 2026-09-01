from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.active import ActiveOrStr


class Activeindicator(SdkBaseModel):
    active: Optional[ActiveOrStr] = UNSET
    """A flag to indicate of the trigger is active, true, or not, false"""


class ActiveindicatorDict(TypedDict):
    active: NotRequired[ActiveOrStr]
