from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_friction_info import ContentFrictionInfo, ContentFrictionInfoDict
from .enums.frame_type import FrameTypeOrStr
from .geographical_path import GeographicalPath, GeographicalPathDict
from .unions.content import Content, ContentDict
from .unions.msg_id import MsgId, MsgIdDict


class DataFrame(SdkBaseModel):
    """The data frame allows sending various advisory and road sign types of information to equipped devices."""

    do_not_use1: Optional[int] = Field(default=UNSET, alias="doNotUse1")
    """Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility."""

    frame_type: FrameTypeOrStr = Field(alias="frameType")
    """The frameType data element provides the type of message to follow in the rest of the message frame structure. The
    following frame types are supported:
     - unknown
     - advisory
     - roadSignage
     - commercialSignage"""

    msg_id: MsgId = Field(alias="msgId")
    start_year: Optional[int] = Field(default=UNSET, alias="startYear")
    """The V2X year consists of integer values from zero to 4095 representing the year according to the Gregorian
    calendar date system. The value of zero shall represent an unknown value."""

    start_time: int = Field(alias="startTime")
    """Start time expresses the number of elapsed minutes of the current year in the time system being used (typically
    UTC time). The value 527040 shall be used for invalid."""

    duration_time: int = Field(alias="durationTime")
    """The duration, in units of whole minutes, that a object persists for. A value of 32000 means that the object
    persists forever. The range 0..32000 provides for about 22.2 days of maximum duration."""

    priority: int
    """The relative importance of the sign, on a scale from zero (least important) to seven (most important)."""

    do_not_use2: Optional[int] = Field(default=UNSET, alias="doNotUse2")
    """Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility."""

    regions: list[GeographicalPath]
    """The data frame is used to support the cross-cutting need in many V2X messages to describe arbitrary spatial areas
    (polygons, boundary lines, and other basic shapes) required by various message types in a small message size. This
    data frame can describe a complex path or region of arbitrary size using either one of the two supported node offset
    methods (XY offsets or LL offsets) or using simple geometric projections."""

    do_not_use3: Optional[int] = Field(default=UNSET, alias="doNotUse3")
    """Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility."""

    do_not_use4: Optional[int] = Field(default=UNSET, alias="doNotUse4")
    """Always set to 0 and carries no meaning. Legacy field maintained for backward compatibility."""

    content: Content
    content_new: Optional[ContentFrictionInfo] = Field(default=UNSET, alias="contentNew")
    """It contains information that extends the original traveler data frame to enable addition of future entities.
    Friction information is the first entity included in the new part three content."""


class DataFrameDict(TypedDict):
    do_not_use1: NotRequired[int]
    frame_type: FrameTypeOrStr
    msg_id: MsgId | MsgIdDict
    start_year: NotRequired[int]
    start_time: int
    duration_time: int
    priority: int
    do_not_use2: NotRequired[int]
    regions: list[GeographicalPath | GeographicalPathDict]
    do_not_use3: NotRequired[int]
    do_not_use4: NotRequired[int]
    content: Content | ContentDict
    content_new: NotRequired[ContentFrictionInfo | ContentFrictionInfoDict]
