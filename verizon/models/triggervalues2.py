from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .promo_alert import PromoAlert, PromoAlertDict


class Triggervalues2(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    promo_alerts: Optional[list[PromoAlert]] = Field(default=UNSET, alias="promoAlerts")
    active: Optional[bool] = UNSET
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    modified_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="modifiedAt")


class Triggervalues2Dict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    account_name: NotRequired[str]
    organization_name: NotRequired[str]
    trigger_category: NotRequired[str]
    promo_alerts: NotRequired[list[PromoAlert | PromoAlertDict]]
    active: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    modified_at: NotRequired[RFC3339DateTime]
