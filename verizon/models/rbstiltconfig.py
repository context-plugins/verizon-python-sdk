from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rbs_high_precision_tilt_config import RbsHighPrecisionTiltConfig, RbsHighPrecisionTiltConfigDict


class Rbstiltconfig(SdkBaseModel):
    rbs_high_precision_tilt_config: Optional[RbsHighPrecisionTiltConfig] = Field(
        default=UNSET, alias="RbsHighPrecisionTiltConfig"
    )


class RbstiltconfigDict(TypedDict):
    rbs_high_precision_tilt_config: NotRequired[RbsHighPrecisionTiltConfig | RbsHighPrecisionTiltConfigDict]
