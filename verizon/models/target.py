from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Target(SdkBaseModel):
    """Target resource definition."""

    address: Optional[str] = UNSET
    """The endpoint for data streams."""

    addressscheme: Optional[str] = UNSET
    """The transport format."""

    billingaccountid: Optional[str] = UNSET
    """The billing account ID."""

    createdon: Optional[str] = UNSET
    """The date the resource was created."""

    externalid: Optional[str] = UNSET
    """Security identification string."""

    id: Optional[str] = UNSET
    """ThingSpace unique ID for the target that was created."""

    kind: Optional[str] = UNSET
    """Identifies the resource kind. Targets are ts.target."""

    lastupdated: Optional[str] = UNSET
    """The date the resource was last updated."""

    name: Optional[str] = UNSET
    """Name of the target."""

    region: Optional[str] = UNSET
    """AWS region value."""

    version: Optional[str] = UNSET
    """Version of the underlying schema resource."""

    versionid: Optional[str] = UNSET
    """The version of the resource."""

    description: Optional[str] = UNSET
    """Description of the target."""


class TargetDict(TypedDict):
    address: NotRequired[str]
    addressscheme: NotRequired[str]
    billingaccountid: NotRequired[str]
    createdon: NotRequired[str]
    externalid: NotRequired[str]
    id: NotRequired[str]
    kind: NotRequired[str]
    lastupdated: NotRequired[str]
    name: NotRequired[str]
    region: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
    description: NotRequired[str]
