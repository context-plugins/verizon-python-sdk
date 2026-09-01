from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorResponseCode(str, Enum):
    """Error Code."""

    UNAUTHORIZED = "UNAUTHORIZED"
    INVALID_ACCESS = "INVALID_ACCESS"
    INVALID_PARAMETER = "INVALID_PARAMETER"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    SUCCESS = "SUCCESS"

    __str__ = str.__str__


ErrorResponseCodeOrStr: TypeAlias = Annotated[ErrorResponseCode | str, open_enum_validator(ErrorResponseCode)]
