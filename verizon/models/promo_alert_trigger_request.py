from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PromoAlertTriggerRequest(SdkBaseModel):
    data_percentage50: Optional[bool] = Field(default=UNSET, alias="dataPercentage50")
    data_percentage75: Optional[bool] = Field(default=UNSET, alias="dataPercentage75")
    data_percentage90: Optional[bool] = Field(default=UNSET, alias="dataPercentage90")
    no_of_days_b4_promo_exp: Optional[int] = Field(default=UNSET, alias="noOfDaysB4PromoExp")
    sms_percentage50: Optional[bool] = Field(default=UNSET, alias="smsPercentage50")
    sms_percentage75: Optional[bool] = Field(default=UNSET, alias="smsPercentage75")
    sms_percentage90: Optional[bool] = Field(default=UNSET, alias="smsPercentage90")


class PromoAlertTriggerRequestDict(TypedDict):
    data_percentage50: NotRequired[bool]
    data_percentage75: NotRequired[bool]
    data_percentage90: NotRequired[bool]
    no_of_days_b4_promo_exp: NotRequired[int]
    sms_percentage50: NotRequired[bool]
    sms_percentage75: NotRequired[bool]
    sms_percentage90: NotRequired[bool]
