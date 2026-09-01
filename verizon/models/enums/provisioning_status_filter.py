from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProvisioningStatusFilter(str, Enum):
    """The last status of the device as a list filter."""

    UNKNOWN = "UNKNOWN"
    DEACTIVATED = "DEACTIVATED"
    ACTIVATED = "ACTIVATED"
    DEACTIVE = "DEACTIVE"
    ACTIVE = "ACTIVE"
    SUSPEND = "SUSPEND"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    PENDING_DEACTIVATION = "PENDING_DEACTIVATION"
    PRE_ACTIVE = "PRE_ACTIVE"
    ACTIVATION_READY = "ACTIVATION_READY"
    INVENTORY = "INVENTORY"
    PURGED = "PURGED"
    REPLACED = "REPLACED"
    RETIRED = "RETIRED"
    TEST_READY = "TEST_READY"

    __str__ = str.__str__


ProvisioningStatusFilterOrStr: TypeAlias = Annotated[
    ProvisioningStatusFilter | str, open_enum_validator(ProvisioningStatusFilter)
]
