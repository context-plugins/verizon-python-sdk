from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Keyschunk2(SdkBaseModel):
    data_percentage50: Optional[bool] = Field(default=UNSET, alias="dataPercentage50")
    data_percentage75: Optional[bool] = Field(default=UNSET, alias="dataPercentage75")
    data_percentage90: Optional[bool] = Field(default=UNSET, alias="dataPercentage90")
    data_percentage100: Optional[bool] = Field(default=UNSET, alias="dataPercentage100")
    sms_percentage50: Optional[bool] = Field(default=UNSET, alias="smsPercentage50")
    sms_percentage75: Optional[bool] = Field(default=UNSET, alias="smsPercentage75")
    sms_percentage90: Optional[bool] = Field(default=UNSET, alias="smsPercentage90")
    sms_percentage100: Optional[bool] = Field(default=UNSET, alias="smsPercentage100")
    no_of_days_b4_promo_exp: Optional[int] = Field(default=UNSET, alias="NoOfDaysB4PromoExp")


class Keyschunk2Dict(TypedDict):
    data_percentage50: NotRequired[bool]
    data_percentage75: NotRequired[bool]
    data_percentage90: NotRequired[bool]
    data_percentage100: NotRequired[bool]
    sms_percentage50: NotRequired[bool]
    sms_percentage75: NotRequired[bool]
    sms_percentage90: NotRequired[bool]
    sms_percentage100: NotRequired[bool]
    no_of_days_b4_promo_exp: NotRequired[int]
