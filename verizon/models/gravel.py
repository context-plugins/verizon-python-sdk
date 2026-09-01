from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type8 import Type8OrStr


class Gravel(SdkBaseModel):
    """Indicates the surface of the roadway is gravel."""

    type_: Optional[Type8OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of gravel."""


class GravelDict(TypedDict):
    type_: NotRequired[Type8OrStr]
