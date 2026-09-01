from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Activate(SdkBaseModel):
    profile: str


class ActivateDict(TypedDict):
    profile: str
