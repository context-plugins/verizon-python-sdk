from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type11 import Type11OrStr


class Rock(SdkBaseModel):
    """Indicates the surface of the roadway is rock."""

    type_: Optional[Type11OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of rock."""


class RockDict(TypedDict):
    type_: NotRequired[Type11OrStr]
