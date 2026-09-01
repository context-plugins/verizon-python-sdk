from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type13 import Type13OrStr


class Snow(SdkBaseModel):
    """Indicates the surface of the roadway is snow."""

    type_: Optional[Type13OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of snow."""


class SnowDict(TypedDict):
    type_: NotRequired[Type13OrStr]
