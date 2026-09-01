from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type12 import Type12OrStr


class Ice(SdkBaseModel):
    """Indicates the surface of the roadway is ice."""

    type_: Optional[Type12OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of ice."""


class IceDict(TypedDict):
    type_: NotRequired[Type12OrStr]
