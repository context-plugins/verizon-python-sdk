from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestStatus(str, Enum):
    """The current status of the callback response."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"

    __str__ = str.__str__


RequestStatusOrStr: TypeAlias = Annotated[RequestStatus | str, open_enum_validator(RequestStatus)]
