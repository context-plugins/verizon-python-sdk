from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kv_pairforplanner import KvPairforplanner, KvPairforplannerDict


class ServicePlanResponseforplanner(SdkBaseModel):
    carrier_service_plan_code: Optional[str] = Field(default=UNSET, alias="carrierServicePlanCode")
    """The name of the service plan code"""

    code: Optional[str] = UNSET
    """The actiavtion code value."""

    extended_attributes: Optional[list[KvPairforplanner]] = Field(default=UNSET, alias="extendedAttributes")
    """key/value pairs assigned by the user for filtering."""

    name: Optional[str] = UNSET
    """The carrier name of the active profile."""

    size_kb: Optional[int] = Field(default=UNSET, alias="sizeKb")
    """size in Kilobytes of the service plan"""


class ServicePlanResponseforplannerDict(TypedDict):
    carrier_service_plan_code: NotRequired[str]
    code: NotRequired[str]
    extended_attributes: NotRequired[list[KvPairforplanner | KvPairforplannerDict]]
    name: NotRequired[str]
    size_kb: NotRequired[int]
