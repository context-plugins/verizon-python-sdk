from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fields_http_headers import FieldsHttpHeaders, FieldsHttpHeadersDict


class CreateTargetRequestFields(SdkBaseModel):
    httpheaders: Optional[FieldsHttpHeaders] = UNSET
    devicetypes: Optional[list[str]] = UNSET
    """List of device types."""


class CreateTargetRequestFieldsDict(TypedDict):
    httpheaders: NotRequired[FieldsHttpHeaders | FieldsHttpHeadersDict]
    devicetypes: NotRequired[list[str]]
