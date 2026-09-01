from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeviceIdforplanner(SdkBaseModel):
    kind: OptionalNullable[str] = UNSET
    id: OptionalNullable[str] = UNSET


class DeviceIdforplannerDict(TypedDict):
    kind: NotRequired[str | None]
    id: NotRequired[str | None]
