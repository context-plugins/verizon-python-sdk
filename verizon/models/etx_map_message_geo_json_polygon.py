from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.etxexpected_type_enum import EtxexpectedTypeEnumOrStr
from .enums.etxmessage_standard_enum import EtxmessageStandardEnumOrStr


class EtxMapMessageGeoJsonPolygon(SdkBaseModel):
    """Query MAP records using a GeoJSON polygon to define the spatial area"""

    message_standard: Optional[EtxmessageStandardEnumOrStr] = Field(default=UNSET, alias="messageStandard")
    """V2X messaging standard selection. Accepted values are 'sae' (SAE J2735) and 'etsi' (ETSI TS 103 301)."""

    geo_json: Any = Field(alias="geoJson")
    """GeoJSON Polygon defining the area to retrieve MAP messages for."""

    expected_type: Optional[EtxexpectedTypeEnumOrStr] = Field(default=UNSET, alias="expectedType")
    """The format of the payload in the response body."""

    page_token: Optional[str] = Field(default=UNSET, alias="pageToken")
    """Base64 encoded token used to retrieve the next page of results"""

    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    """Maximum number of records to return in a single page"""


class EtxMapMessageGeoJsonPolygonDict(TypedDict):
    message_standard: NotRequired[EtxmessageStandardEnumOrStr]
    geo_json: Any
    expected_type: NotRequired[EtxexpectedTypeEnumOrStr]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
