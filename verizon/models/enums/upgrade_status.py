from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UpgradeStatus(str, Enum):
    """The status of the upgrades that you want to retrieve."""

    REQUEST_PENDING = "RequestPending"
    QUEUED = "Queued"
    REQUEST_FAILED = "RequestFailed"
    IN_PROGRESS = "InProgress"
    FINISHED = "Finished"
    UPGRADE_FAILED = "UpgradeFailed"

    __str__ = str.__str__


UpgradeStatusOrStr: TypeAlias = Annotated[UpgradeStatus | str, open_enum_validator(UpgradeStatus)]
