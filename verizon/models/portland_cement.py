from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type6 import Type6OrStr


class PortlandCement(SdkBaseModel):
    """Indicates the surface of the roadway is portland cement."""

    type_: Optional[Type6OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of portland cement."""


class PortlandCementDict(TypedDict):
    type_: NotRequired[Type6OrStr]
