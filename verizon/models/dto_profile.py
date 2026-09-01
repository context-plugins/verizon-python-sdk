from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoProfile(SdkBaseModel):
    kind: Optional[str] = UNSET
    """profile kind"""

    version: Optional[str] = UNSET
    """The resource version"""

    modelid: Optional[str] = UNSET
    """device model id"""

    name: Optional[str] = UNSET
    """profile name"""

    configuration: Optional[Any] = UNSET


class DtoProfileDict(TypedDict):
    kind: NotRequired[str]
    version: NotRequired[str]
    modelid: NotRequired[str]
    name: NotRequired[str]
    configuration: NotRequired[Any]
