from __future__ import annotations

from typing import TypeAlias

from ..account_group_share_update_trigger_request import (
    AccountGroupShareUpdateTriggerRequest,
    AccountGroupShareUpdateTriggerRequestDict,
)
from ..account_level_update_trigger_request import (
    AccountLevelUpdateTriggerRequest,
    AccountLevelUpdateTriggerRequestDict,
)
from ..account_share_update_trigger_request import (
    AccountShareUpdateTriggerRequest,
    AccountShareUpdateTriggerRequestDict,
)
from ..device_level_update_trigger_request import DeviceLevelUpdateTriggerRequest, DeviceLevelUpdateTriggerRequestDict
from ..pay_as_you_go_update_trigger_request import PayAsYouGoUpdateTriggerRequest, PayAsYouGoUpdateTriggerRequestDict
from ..updatetriggerchunk import Updatetriggerchunk, UpdatetriggerchunkDict

V2TriggersRequest1: TypeAlias = (
    AccountLevelUpdateTriggerRequest
    | DeviceLevelUpdateTriggerRequest
    | AccountGroupShareUpdateTriggerRequest
    | AccountShareUpdateTriggerRequest
    | PayAsYouGoUpdateTriggerRequest
    | Updatetriggerchunk
)

V2TriggersRequest1Dict: TypeAlias = (
    AccountLevelUpdateTriggerRequestDict
    | DeviceLevelUpdateTriggerRequestDict
    | AccountGroupShareUpdateTriggerRequestDict
    | AccountShareUpdateTriggerRequestDict
    | PayAsYouGoUpdateTriggerRequestDict
    | UpdatetriggerchunkDict
)
