from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type10 import Type10OrStr


class Cinders(SdkBaseModel):
    """Indicates the surface of the roadway is cinders."""

    type_: Optional[Type10OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of cinders."""


class CindersDict(TypedDict):
    type_: NotRequired[Type10OrStr]
