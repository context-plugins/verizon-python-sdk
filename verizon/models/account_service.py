from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .state import State, StateDict


class AccountService(SdkBaseModel):
    """Service associated with the account."""

    name: Optional[str] = UNSET
    """The name of the service plan."""

    description: Optional[str] = UNSET
    """The description of the service plan."""

    states: Optional[list[State]] = UNSET
    """The state of the service plan."""


class AccountServiceDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    states: NotRequired[list[State | StateDict]]
