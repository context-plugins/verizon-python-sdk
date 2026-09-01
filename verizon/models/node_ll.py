from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .node_offset_point_ll import NodeOffsetPointLl, NodeOffsetPointLlDict


class NodeLl(SdkBaseModel):
    """The NodeLL data frame presents a structure to hold data for a signal node point in a lane. Each selected node has
    a complete lat-long representation."""

    delta: NodeOffsetPointLl
    """The NodeOffsetPointLL data frame presents a structure to hold 64 bits sized data frames for a single node
    geometry path. Nodes are described in terms of latitude and longitude."""


class NodeLlDict(TypedDict):
    delta: NodeOffsetPointLl | NodeOffsetPointLlDict
