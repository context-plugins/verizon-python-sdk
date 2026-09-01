from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateIoTapplicationResponse(SdkBaseModel):
    """A success response includes an array of all matching events. Each event includes the full event resource
    definition."""

    app_name: Optional[str] = Field(default=UNSET, alias="appName")
    """An application will be created under the user's Azure subscription with this name and of type IOT central."""

    shared_secret: Optional[str] = Field(default=UNSET, alias="sharedSecret")
    """Part of the user credentials (from Azure) the user needs to use for calling further TS Core APIs for setting up
    Azure cloud connector."""

    url: Optional[str] = UNSET
    """An IOT central endpoint the user can use to see the data that is being streamed."""


class CreateIoTapplicationResponseDict(TypedDict):
    app_name: NotRequired[str]
    shared_secret: NotRequired[str]
    url: NotRequired[str]
