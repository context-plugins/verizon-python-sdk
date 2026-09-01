from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaeAlertPayload(SdkBaseModel):
    """Road Side Alert (RSA) message payload as defined in SAE J2735."""

    msg_cnt: Optional[int] = Field(default=UNSET, alias="msgCnt")
    """It is used to provide a sequence number within a stream of messages with the same DSRCmsgID (here RoadSideAlert)
    and from the same sender."""

    type_event: int = Field(alias="typeEvent")
    """The ITIS Code that describes the alert/danger/hazard. All ITS standards use the same types here to explain the
    type of the alert/danger/hazard involved.

    The complete set of ITIS codes can be found in Volume Two of the SAE J2540 standard. This is a set of over 1000
    items which are used to encode common events and list items in ITS."""

    description: Optional[list[int]] = UNSET
    """ITIS code set entries to further describe the event, give advice, or any other ITIS codes related to the
    event/danger/hazard."""


class SaeAlertPayloadDict(TypedDict):
    msg_cnt: NotRequired[int]
    type_event: int
    description: NotRequired[list[int]]
