from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .status_list import StatusList, StatusListDict


class ManagedAccountsAddResponse(SdkBaseModel):
    tx_id: Optional[str] = Field(default=UNSET, alias="TxId")
    """Transaction identifier"""

    status_list: Optional[list[StatusList]] = Field(default=UNSET, alias="statusList")


class ManagedAccountsAddResponseDict(TypedDict):
    tx_id: NotRequired[str]
    status_list: NotRequired[list[StatusList | StatusListDict]]
