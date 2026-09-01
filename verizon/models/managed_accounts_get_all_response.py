from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .managed_acc_added_list import ManagedAccAddedList, ManagedAccAddedListDict
from .managed_acc_provisioned_list import ManagedAccProvisionedList, ManagedAccProvisionedListDict


class ManagedAccountsGetAllResponse(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account Name"""

    managed_acc_added_list: Optional[list[ManagedAccAddedList]] = Field(default=UNSET, alias="ManagedAccAddedList")
    managed_acc_provisioned_list: Optional[list[ManagedAccProvisionedList]] = Field(
        default=UNSET, alias="managedAccProvisionedList"
    )


class ManagedAccountsGetAllResponseDict(TypedDict):
    account_name: NotRequired[str]
    managed_acc_added_list: NotRequired[list[ManagedAccAddedList | ManagedAccAddedListDict]]
    managed_acc_provisioned_list: NotRequired[list[ManagedAccProvisionedList | ManagedAccProvisionedListDict]]
