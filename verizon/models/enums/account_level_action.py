from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountLevelAction(str, Enum):
    """The action taken when trigger conditions are met"""

    NOTIFY = "notify"
    SUSPEND = "suspend"
    CHANGE_PRICE_PLAN = "changePricePlan"

    __str__ = str.__str__


AccountLevelActionOrStr: TypeAlias = Annotated[AccountLevelAction | str, open_enum_validator(AccountLevelAction)]
