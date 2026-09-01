from __future__ import annotations

from typing import TypeAlias

from ..further_info_msg_id import FurtherInfoMsgId, FurtherInfoMsgIdDict
from ..road_sign_msg_id import RoadSignMsgId, RoadSignMsgIdDict

MsgId: TypeAlias = FurtherInfoMsgId | RoadSignMsgId

MsgIdDict: TypeAlias = FurtherInfoMsgIdDict | RoadSignMsgIdDict
