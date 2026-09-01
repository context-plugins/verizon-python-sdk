from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FrameType(str, Enum):
    """The frameType data element provides the type of message to follow in the rest of the message frame structure. The
    following frame types are supported:
     - unknown
     - advisory
     - roadSignage
     - commercialSignage"""

    UNKNOWN = "unknown"
    ADVISORY = "advisory"
    ROAD_SIGNAGE = "roadSignage"
    COMMERCIAL_SIGNAGE = "commercialSignage"

    __str__ = str.__str__


FrameTypeOrStr: TypeAlias = Annotated[FrameType | str, open_enum_validator(FrameType)]
