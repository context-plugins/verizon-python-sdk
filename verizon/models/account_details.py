from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier import Carrier, CarrierDict
from .carrier_service_plan import CarrierServicePlan, CarrierServicePlanDict
from .feature import Feature, FeatureDict


class AccountDetails(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included."""

    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included."""

    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    """user defined name of organization"""

    is_provisioning_allowed: Optional[bool] = Field(default=UNSET, alias="isProvisioningAllowed")
    """Flag set to indicate if account details can be edited or not. Default is "true"."""

    carriers: Optional[list[Carrier]] = UNSET
    features: Optional[list[Feature]] = UNSET
    service_plans: Optional[list[CarrierServicePlan]] = Field(default=UNSET, alias="servicePlans")


class AccountDetailsDict(TypedDict):
    account_name: NotRequired[str]
    account_number: NotRequired[str]
    organization_name: NotRequired[str]
    is_provisioning_allowed: NotRequired[bool]
    carriers: NotRequired[list[Carrier | CarrierDict]]
    features: NotRequired[list[Feature | FeatureDict]]
    service_plans: NotRequired[list[CarrierServicePlan | CarrierServicePlanDict]]
