from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MismatchedDevice(SdkBaseModel):
    """4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time
    frame."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The account that the device is associated with."""

    mdn: Optional[str] = UNSET
    """The assigned phone number of the device."""

    activation_date: Optional[str] = Field(default=UNSET, alias="activationDate")
    """The date and time when the SIM was last activated."""

    iccid: Optional[str] = UNSET
    """The ID of the SIM."""

    pre_imei: Optional[str] = Field(default=UNSET, alias="preImei")
    """The IMEI of the device prior to the SIM OTA activation on simOtaDate."""

    post_imei: Optional[str] = Field(default=UNSET, alias="postImei")
    """The IMEI of the device after the SIM OTA activation on simOtaDate."""

    sim_ota_date: Optional[str] = Field(default=UNSET, alias="simOtaDate")
    """The date and time of the SIM OTA activation."""


class MismatchedDeviceDict(TypedDict):
    account_name: NotRequired[str]
    mdn: NotRequired[str]
    activation_date: NotRequired[str]
    iccid: NotRequired[str]
    pre_imei: NotRequired[str]
    post_imei: NotRequired[str]
    sim_ota_date: NotRequired[str]
