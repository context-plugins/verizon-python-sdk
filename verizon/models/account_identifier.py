from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountIdentifier(SdkBaseModel):
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    billingaccountid: Optional[str] = UNSET


class AccountIdentifierDict(TypedDict):
    billingaccountid: NotRequired[str]
