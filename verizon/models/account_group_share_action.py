from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .notify import Notify, NotifyDict


class AccountGroupShareAction(SdkBaseModel):
    notify: Optional[Notify] = UNSET


class AccountGroupShareActionDict(TypedDict):
    notify: NotRequired[Notify | NotifyDict]
