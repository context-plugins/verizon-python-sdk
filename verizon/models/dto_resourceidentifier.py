from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoResourceidentifier(SdkBaseModel):
    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""


class DtoResourceidentifierDict(TypedDict):
    id: NotRequired[str]
