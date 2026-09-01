from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkUpdateSmartalert(SdkBaseModel):
    name: Optional[str] = UNSET
    """User defined name of the record"""


class BulkUpdateSmartalertDict(TypedDict):
    name: NotRequired[str]
