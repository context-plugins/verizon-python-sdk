from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data_frame import DataFrame, DataFrameDict


class SaeInfoPayload(SdkBaseModel):
    """Traveler Information Message (TIM) payload as defined in SAE J2735."""

    msg_cnt: Optional[int] = Field(default=UNSET, alias="msgCnt")
    """It is used to provide a sequence number within a stream of messages with the same DSRCmsgID (here RoadSideAlert)
    and from the same sender."""

    time_stamp: Optional[int] = Field(default=UNSET, alias="timeStamp")
    """The number of elapsed minutes of the current year in the time system being used (typically UTC time). -- the
    value 527040 shall be used for invalid"""

    packet_id: Optional[str] = Field(default=UNSET, alias="packetID")
    """Provides a relatively unique value which can be used to connect to (link to) other supporting messages in other
    formats.

    The value is described as a 18-character hexadecimal string."""

    url_b: Optional[str] = Field(default=UNSET, alias="urlB")
    """A valid internet style URI/URL in the form of a text string which will form the base of a compound string which,
    when combined with the URL-short data element, will link to the designated resource."""

    data_frames: list[DataFrame] = Field(alias="dataFrames")
    """List of data frames."""


class SaeInfoPayloadDict(TypedDict):
    msg_cnt: NotRequired[int]
    time_stamp: NotRequired[int]
    packet_id: NotRequired[str]
    url_b: NotRequired[str]
    data_frames: list[DataFrame | DataFrameDict]
