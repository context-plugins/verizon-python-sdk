from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FieldsHttpHeaders(SdkBaseModel):
    authorization: Optional[str] = Field(default=UNSET, alias="Authorization")


class FieldsHttpHeadersDict(TypedDict):
    authorization: NotRequired[str]
