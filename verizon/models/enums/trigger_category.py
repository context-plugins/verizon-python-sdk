from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TriggerCategory(str, Enum):
    """The type of trigger being created or modified"""

    ACCOUNT_USAGE = "AccountUsage"
    DEVICE_GROUP_USAGE = "DeviceGroupUsage"
    PRICE_PLAN_DATA_USAGE = "PricePlanDataUsage"

    __str__ = str.__str__


TriggerCategoryOrStr: TypeAlias = Annotated[TriggerCategory | str, open_enum_validator(TriggerCategory)]
