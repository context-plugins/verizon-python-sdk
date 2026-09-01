from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .ippoolforplanner import Ippoolforplanner, IppoolforplannerDict
from .service_plan_responseforplanner import ServicePlanResponseforplanner, ServicePlanResponseforplannerDict


class GetAccountInformationResponseforplanner(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    account_number: OptionalNullable[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric name of the account, including leading zeros."""

    carriers: Optional[list[str]] = UNSET
    """The list of carrier names with profiles."""

    features: Optional[list[str]] = UNSET
    """a list of features associated with the resident profiles."""

    ip_pools: Optional[list[Ippoolforplanner]] = Field(default=UNSET, alias="ipPools")
    is_provisioning_allowed: Optional[bool] = Field(default=UNSET, alias="isProvisioningAllowed")
    """A flag indicating if provisioning is allowed (true) or provisioning is locked (false)."""

    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    """The user assigned organization name."""

    service_plans: Optional[list[ServicePlanResponseforplanner]] = Field(default=UNSET, alias="servicePlans")
    """A list of service plans associated with the resident profiles."""


class GetAccountInformationResponseforplannerDict(TypedDict):
    account_name: NotRequired[str]
    account_number: NotRequired[str | None]
    carriers: NotRequired[list[str]]
    features: NotRequired[list[str]]
    ip_pools: NotRequired[list[Ippoolforplanner | IppoolforplannerDict]]
    is_provisioning_allowed: NotRequired[bool]
    organization_name: NotRequired[str]
    service_plans: NotRequired[list[ServicePlanResponseforplanner | ServicePlanResponseforplannerDict]]
