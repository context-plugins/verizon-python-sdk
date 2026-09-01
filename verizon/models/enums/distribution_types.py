from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DistributionTypes(str, Enum):
    """The distribution types:
      - Targeted: Generate targeted messages to the road users that are affected by the zone rules
      - Broadcast: Broadcast messages to regions based on the Geofence."""

    TARGETED = "Targeted"
    BROADCAST = "Broadcast"

    __str__ = str.__str__


DistributionTypesOrStr: TypeAlias = Annotated[DistributionTypes | str, open_enum_validator(DistributionTypes)]
