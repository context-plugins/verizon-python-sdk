from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NodeLlmD64B(SdkBaseModel):
    """A 64-bit node type with lat-long values expressed in standard SAE 1/10th of a microdegree."""

    lon: int
    """The geographic longitude of an object, expressed in 1/10th integer microdegrees, as a 32-bit value, and with
    reference to the horizontal datum then in use. The value 1800000001 shall be used when unavailable."""

    lat: int
    """The geographic latitude of an object, expressed in 1/10th integer microdegrees, as a 31 bit value, and with
    reference to the horizontal datum then in use. The value 900000001 shall be used when unavailable."""


class NodeLlmD64BDict(TypedDict):
    lon: int
    lat: int
