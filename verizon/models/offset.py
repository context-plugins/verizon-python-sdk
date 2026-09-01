from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .node_list_ll import NodeListLl, NodeListLlDict


class Offset(SdkBaseModel):
    """The sequence of node offsets then describes a path or polygon in the Lat-Long system."""

    ll: NodeListLl
    """The NodeListLL data structure provides the sequence of signed offset node point values for determining the
    latitude and longitude. Each LL point is referred to as a node point."""


class OffsetDict(TypedDict):
    ll: NodeListLl | NodeListLlDict
