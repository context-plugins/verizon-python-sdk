from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StatusList(SdkBaseModel):
    id: Optional[str] = UNSET
    """Account name"""

    status: Optional[str] = UNSET
    """Success or Fail"""

    reason: Optional[str] = UNSET
    """detailed reason"""


class StatusListDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[str]
    reason: NotRequired[str]
