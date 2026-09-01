from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .generate_response_item_credential import GenerateResponseItemCredential, GenerateResponseItemCredentialDict


class GenerateResponseItem(SdkBaseModel):
    imei: Optional[str] = UNSET
    credential: Optional[GenerateResponseItemCredential] = UNSET


class GenerateResponseItemDict(TypedDict):
    imei: NotRequired[str]
    credential: NotRequired[GenerateResponseItemCredential | GenerateResponseItemCredentialDict]
