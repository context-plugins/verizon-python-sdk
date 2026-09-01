from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_sub_rest_error_responseforplanner import (
    AuthSubRestErrorResponseforplanner,
    AuthSubRestErrorResponseforplannerDict,
)


class AuthRestErrorResponseforplanner(SdkBaseModel):
    fault: Optional[AuthSubRestErrorResponseforplanner] = UNSET


class AuthRestErrorResponseforplannerDict(TypedDict):
    fault: NotRequired[AuthSubRestErrorResponseforplanner | AuthSubRestErrorResponseforplannerDict]
