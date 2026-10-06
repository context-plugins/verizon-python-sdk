from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.type6 import Type6, Type6OrStr


class PortlandCement(SdkBaseModel):
    """Indicates the surface of the roadway is portland cement."""

    type_: Type6OrStr = Field(default=Type6.TRAVELED, alias="type")
    """Indicates the type of portland cement."""


class PortlandCementDict(TypedDict):
    type_: NotRequired[Type6OrStr]
