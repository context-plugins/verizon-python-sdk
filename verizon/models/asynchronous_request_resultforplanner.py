from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AsynchronousRequestResultforplanner(SdkBaseModel):
    """A successful request returns the request ID (UUID) and the current status."""

    request_id: OptionalNullable[str] = Field(default=UNSET, alias="requestId")
    """The unique ID of a request. This is a UUID value."""


class AsynchronousRequestResultforplannerDict(TypedDict):
    request_id: NotRequired[str | None]
