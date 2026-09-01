from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .flow_info import FlowInfo, FlowInfoDict
from .qosdevice_id import QosdeviceId, QosdeviceIdDict


class QosdeviceInfo(SdkBaseModel):
    device_id: QosdeviceId = Field(alias="deviceId")
    device_i_pv6_addr: Optional[str] = Field(default=UNSET, alias="deviceIPv6Addr")
    flow_info: list[FlowInfo] = Field(alias="flowInfo")


class QosdeviceInfoDict(TypedDict):
    device_id: QosdeviceId | QosdeviceIdDict
    device_i_pv6_addr: NotRequired[str]
    flow_info: list[FlowInfo | FlowInfoDict]
