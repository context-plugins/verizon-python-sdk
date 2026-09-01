from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AwarenessDistance(str, Enum):
    """Specifies how far the event is relevant to."""

    LESS_THAN50M = "lessThan50m"
    LESS_THAN100M = "lessThan100m"
    LESS_THAN200M = "lessThan200m"
    LESS_THAN500M = "lessThan500m"
    LESS_THAN1000M = "lessThan1000m"
    LESS_THAN5KM = "lessThan5km"
    LESS_THAN10KM = "lessThan10km"
    OVER10KM = "over10km"

    __str__ = str.__str__


AwarenessDistanceOrStr: TypeAlias = Annotated[AwarenessDistance | str, open_enum_validator(AwarenessDistance)]
