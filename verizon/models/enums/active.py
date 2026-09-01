from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Active(str, Enum):
    """A flag to indicate of the trigger is active, true, or not, false"""

    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


ActiveOrStr: TypeAlias = Annotated[Active | str, open_enum_validator(Active)]
