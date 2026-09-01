from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .node_llm_d64_b import NodeLlmD64B, NodeLlmD64BDict


class NodeOffsetPointLl(SdkBaseModel):
    """The NodeOffsetPointLL data frame presents a structure to hold 64 bits sized data frames for a single node
    geometry path. Nodes are described in terms of latitude and longitude."""

    node_lat_lon: NodeLlmD64B = Field(alias="node-LatLon")
    """A 64-bit node type with lat-long values expressed in standard SAE 1/10th of a microdegree."""


class NodeOffsetPointLlDict(TypedDict):
    node_lat_lon: NodeLlmD64B | NodeLlmD64BDict
