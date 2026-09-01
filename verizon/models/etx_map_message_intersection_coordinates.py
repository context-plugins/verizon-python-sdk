from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.etxexpected_type_enum import EtxexpectedTypeEnumOrStr
from .enums.etxmessage_standard_enum import EtxmessageStandardEnumOrStr
from .region_intersection_pair import RegionIntersectionPair, RegionIntersectionPairDict


class EtxMapMessageIntersectionCoordinates(SdkBaseModel):
    """Query MAP records using specific region and intersection identifier pairs"""

    message_standard: Optional[EtxmessageStandardEnumOrStr] = Field(default=UNSET, alias="messageStandard")
    """V2X messaging standard selection. Accepted values are 'sae' (SAE J2735) and 'etsi' (ETSI TS 103 301)."""

    region_intersection_pairs: list[RegionIntersectionPair] = Field(alias="regionIntersectionPairs")
    """List of region and intersection ID pairs to retrieve MAP messages for."""

    expected_type: Optional[EtxexpectedTypeEnumOrStr] = Field(default=UNSET, alias="expectedType")
    """The format of the payload in the response body."""

    page_token: Optional[str] = Field(default=UNSET, alias="pageToken")
    """Base64 encoded token used to retrieve the next page of results"""

    page_size: Optional[int] = Field(default=UNSET, alias="pageSize")
    """Maximum number of records to return in a single page"""


class EtxMapMessageIntersectionCoordinatesDict(TypedDict):
    message_standard: NotRequired[EtxmessageStandardEnumOrStr]
    region_intersection_pairs: list[RegionIntersectionPair | RegionIntersectionPairDict]
    expected_type: NotRequired[EtxexpectedTypeEnumOrStr]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
