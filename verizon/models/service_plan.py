from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class ServicePlan(SdkBaseModel):
    """Details of the service plan."""

    carrier_service_plan_code: Optional[str] = Field(default=UNSET, alias="carrierServicePlanCode")
    """The code that is used by the carrier for the service plan."""

    code: Optional[str] = UNSET
    """The code of the service plan, which may not be the same as the name."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """Any extended attributes for the service plan, as Key and Value pairs."""

    name: Optional[str] = UNSET
    """The name of the service plan."""

    size_kb: Optional[int] = Field(default=UNSET, alias="sizeKb")
    """The size of the service plan in kilobytes."""


class ServicePlanDict(TypedDict):
    carrier_service_plan_code: NotRequired[str]
    code: NotRequired[str]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    name: NotRequired[str]
    size_kb: NotRequired[int]
