from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type9 import Type9OrStr


class Grass(SdkBaseModel):
    """Indicates the surface of the roadway is grass."""

    type_: Optional[Type9OrStr] = Field(default=UNSET, alias="type")
    """Indicates the surface of the roadway is grass with low speed limit."""


class GrassDict(TypedDict):
    type_: NotRequired[Type9OrStr]
