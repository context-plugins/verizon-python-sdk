from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HyperPreciseLocationCallback(SdkBaseModel):
    """Callback registration request."""

    name: str
    """The name of the callback service that you want to subscribe to."""

    url: str
    """The address on your server where you have enabled a listening service for the specific type of callback messages.
    Specify a URL that is reachable from the Verizon data centers. If your service is running on HTTPS, you should use a
    one-way authentication certificate with a white-listed IP address."""


class HyperPreciseLocationCallbackDict(TypedDict):
    name: str
    url: str
