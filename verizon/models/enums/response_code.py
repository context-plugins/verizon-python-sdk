from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResponseCode(str, Enum):
    """Possible response codes."""

    INVALID_ACCESS = "INVALID_ACCESS"
    INVALID_PARAMETER = "INVALID_PARAMETER"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    SUCCESS = "SUCCESS"

    __str__ = str.__str__


ResponseCodeOrStr: TypeAlias = Annotated[ResponseCode | str, open_enum_validator(ResponseCode)]
