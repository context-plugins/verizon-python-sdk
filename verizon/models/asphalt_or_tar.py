from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type7 import Type7OrStr


class AsphaltOrTar(SdkBaseModel):
    """Indicates the surface of the roadway is asphalt or tar."""

    type_: Optional[Type7OrStr] = Field(default=UNSET, alias="type")
    """Indicates the type of asphalt or tar."""


class AsphaltOrTarDict(TypedDict):
    type_: NotRequired[Type7OrStr]
