from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProfileStatusFilter(str, Enum):
    """The last status of the device's profile as a filter."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    DOWNLOAD_DISABLE = "DOWNLOAD_DISABLE"
    DOWNLOAD_ENABLE = "DOWNLOAD_ENABLE"
    NOT_DOWNLOADED = "NOT_DOWNLOADED"
    UNKNOWN = "UNKNOWN"
    DELETE = "DELETE"

    __str__ = str.__str__


ProfileStatusFilterOrStr: TypeAlias = Annotated[ProfileStatusFilter | str, open_enum_validator(ProfileStatusFilter)]
