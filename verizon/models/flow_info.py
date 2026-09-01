from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FlowInfo(SdkBaseModel):
    flow_server: Optional[str] = Field(default=UNSET, alias="flowServer")
    flow_device: Optional[str] = Field(default=UNSET, alias="flowDevice")
    flow_direction: Optional[str] = Field(default=UNSET, alias="flowDirection")
    flow_protocol: Optional[str] = Field(default=UNSET, alias="flowProtocol")
    qci_option: Optional[str] = Field(default=UNSET, alias="qciOption")


class FlowInfoDict(TypedDict):
    flow_server: NotRequired[str]
    flow_device: NotRequired[str]
    flow_direction: NotRequired[str]
    flow_protocol: NotRequired[str]
    qci_option: NotRequired[str]
