from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .geographical_path_description import GeographicalPathDescription, GeographicalPathDescriptionDict


class GeographicalPath(SdkBaseModel):
    """The data frame is used to support the cross-cutting need in many V2X messages to describe arbitrary spatial areas
    (polygons, boundary lines, and other basic shapes) required by various message types in a small message size."""

    description: Optional[GeographicalPathDescription] = UNSET
    """This data frame can describe a complex path of arbitrary size using node offset method (LL offsets)."""

    direction: Optional[str] = UNSET
    """OctetStrings are described as hexadecimal strings, where each octet is represented by two hexadecimal
    characters."""


class GeographicalPathDict(TypedDict):
    description: NotRequired[GeographicalPathDescription | GeographicalPathDescriptionDict]
    direction: NotRequired[str]
