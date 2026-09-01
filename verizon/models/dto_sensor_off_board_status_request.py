from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gatewayidentifier import Gatewayidentifier, GatewayidentifierDict
from .offboarding import Offboarding, OffboardingDict


class DtoSensorOffBoardStatusRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    gatewayidentifier: Optional[Gatewayidentifier] = UNSET
    offboarding: Optional[Offboarding] = UNSET


class DtoSensorOffBoardStatusRequestDict(TypedDict):
    accountname: NotRequired[str]
    gatewayidentifier: NotRequired[Gatewayidentifier | GatewayidentifierDict]
    offboarding: NotRequired[Offboarding | OffboardingDict]
