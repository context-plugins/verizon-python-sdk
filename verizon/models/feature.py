from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Feature(SdkBaseModel):
    features: Optional[str] = UNSET
    """The calling and data features available for the account. **Note:** for Global IoT Orchestrator, the features
    ``eUICC Verizon as Lead`` and ``Global eSim Billing`` will always be present."""


class FeatureDict(TypedDict):
    features: NotRequired[str]
