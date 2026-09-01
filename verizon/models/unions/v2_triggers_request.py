from __future__ import annotations

from typing import TypeAlias

from ..account_group_share_create_trigger_request import (
    AccountGroupShareCreateTriggerRequest,
    AccountGroupShareCreateTriggerRequestDict,
)
from ..account_level_create_trigger_request import (
    AccountLevelCreateTriggerRequest,
    AccountLevelCreateTriggerRequestDict,
)
from ..account_level_object import AccountLevelObject, AccountLevelObjectDict
from ..account_share_create_trigger_request import (
    AccountShareCreateTriggerRequest,
    AccountShareCreateTriggerRequestDict,
)
from ..createtriggerchunk import Createtriggerchunk, CreatetriggerchunkDict
from ..device_level_create_trigger_request import DeviceLevelCreateTriggerRequest, DeviceLevelCreateTriggerRequestDict
from ..pay_as_you_go_create_trigger_request import PayAsYouGoCreateTriggerRequest, PayAsYouGoCreateTriggerRequestDict

V2TriggersRequest: TypeAlias = (
    AccountLevelCreateTriggerRequest
    | AccountLevelObject
    | DeviceLevelCreateTriggerRequest
    | AccountGroupShareCreateTriggerRequest
    | AccountShareCreateTriggerRequest
    | PayAsYouGoCreateTriggerRequest
    | Createtriggerchunk
)

V2TriggersRequestDict: TypeAlias = (
    AccountLevelCreateTriggerRequestDict
    | AccountLevelObjectDict
    | DeviceLevelCreateTriggerRequestDict
    | AccountGroupShareCreateTriggerRequestDict
    | AccountShareCreateTriggerRequestDict
    | PayAsYouGoCreateTriggerRequestDict
    | CreatetriggerchunkDict
)
