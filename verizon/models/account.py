from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ippool import Ippool, IppoolDict
from .service_plan import ServicePlan, ServicePlanDict


class Account(SdkBaseModel):
    """Returns information about a specified account."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the account."""

    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The billing number of the account."""

    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    """The name of the organization that the account is part of."""

    is_provisioning_allowed: Optional[bool] = Field(default=UNSET, alias="isProvisioningAllowed")
    """True if devices can be added to the account and activated with a single request. False if devices must be added
    to the account before they can be activated."""

    carriers: Optional[list[str]] = UNSET
    """The names of all carriers for the account."""

    features: Optional[list[str]] = UNSET
    """The names of features that are enabled for the account."""

    i_p_pools: Optional[list[Ippool]] = Field(default=UNSET, alias="iPPools")
    """Array of IP pools that are available to the account."""

    service_plans: Optional[list[ServicePlan]] = Field(default=UNSET, alias="servicePlans")
    """Array of service plans that are available to the account."""


class AccountDict(TypedDict):
    account_name: NotRequired[str]
    account_number: NotRequired[str]
    organization_name: NotRequired[str]
    is_provisioning_allowed: NotRequired[bool]
    carriers: NotRequired[list[str]]
    features: NotRequired[list[str]]
    i_p_pools: NotRequired[list[Ippool | IppoolDict]]
    service_plans: NotRequired[list[ServicePlan | ServicePlanDict]]
