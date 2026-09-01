from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RetrieveResponseItem(SdkBaseModel):
    imei: Optional[str] = UNSET
    username: Optional[str] = UNSET
    """Present if credentials exist"""

    failure: Optional[str] = UNSET
    """Present if retrieval failed"""


class RetrieveResponseItemDict(TypedDict):
    imei: NotRequired[str]
    username: NotRequired[str]
    failure: NotRequired[str]
