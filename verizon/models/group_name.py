from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GroupName(SdkBaseModel):
    default: Optional[str] = Field(default=UNSET, alias="Default")


class GroupNameDict(TypedDict):
    default: NotRequired[str]
