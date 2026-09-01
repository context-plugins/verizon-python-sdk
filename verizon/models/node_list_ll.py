from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .node_ll import NodeLl, NodeLlDict


class NodeListLl(SdkBaseModel):
    """The NodeListLL data structure provides the sequence of signed offset node point values for determining the
    latitude and longitude. Each LL point is referred to as a node point."""

    nodes: list[NodeLl]
    """The NodeSetLL data frame consists of a list of NodeLL entries using LL offsets."""


class NodeListLlDict(TypedDict):
    nodes: list[NodeLl | NodeLlDict]
