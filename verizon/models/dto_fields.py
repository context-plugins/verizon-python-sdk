from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoFields(SdkBaseModel):
    """Fields to return needed by search"""

    additional_prop1: Optional[str] = Field(default=UNSET, alias="additionalProp1")
    additional_prop2: Optional[str] = Field(default=UNSET, alias="additionalProp2")
    additional_prop3: Optional[str] = Field(default=UNSET, alias="additionalProp3")


class DtoFieldsDict(TypedDict):
    additional_prop1: NotRequired[str]
    additional_prop2: NotRequired[str]
    additional_prop3: NotRequired[str]
