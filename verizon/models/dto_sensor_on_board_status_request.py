from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gatewayidentifier import Gatewayidentifier, GatewayidentifierDict
from .onboarding import Onboarding, OnboardingDict


class DtoSensorOnBoardStatusRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    gatewayidentifier: Optional[Gatewayidentifier] = UNSET
    onboarding: Optional[Onboarding] = UNSET


class DtoSensorOnBoardStatusRequestDict(TypedDict):
    accountname: NotRequired[str]
    gatewayidentifier: NotRequired[Gatewayidentifier | GatewayidentifierDict]
    onboarding: NotRequired[Onboarding | OnboardingDict]
