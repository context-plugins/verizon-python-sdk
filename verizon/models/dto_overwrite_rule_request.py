from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_resourceidentifier import DtoResourceidentifier, DtoResourceidentifierDict
from .resource_rule import ResourceRule, ResourceRuleDict


class DtoOverwriteRuleRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    resourceidentifier: Optional[DtoResourceidentifier] = UNSET
    rule: Optional[ResourceRule] = UNSET


class DtoOverwriteRuleRequestDict(TypedDict):
    accountname: NotRequired[str]
    resourceidentifier: NotRequired[DtoResourceidentifier | DtoResourceidentifierDict]
    rule: NotRequired[ResourceRule | ResourceRuleDict]
