from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .friction_information import FrictionInformation, FrictionInformationDict


class ContentFrictionInfo(SdkBaseModel):
    friction_info: FrictionInformation = Field(alias="frictionInfo")


class ContentFrictionInfoDict(TypedDict):
    friction_info: FrictionInformation | FrictionInformationDict
