from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .promo_alert1 import PromoAlert1, PromoAlert1Dict


class RequestTrigger(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    promo_alerts: Optional[list[PromoAlert1]] = Field(default=UNSET, alias="promoAlerts")


class RequestTriggerDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    account_name: NotRequired[str]
    organization_name: NotRequired[str]
    trigger_category: NotRequired[str]
    promo_alerts: NotRequired[list[PromoAlert1 | PromoAlert1Dict]]
