from __future__ import annotations

from typing import TypeAlias

from ..condition_object_call import ConditionObjectCall, ConditionObjectCallDict
from ..enums.condition_type import ConditionTypeOrStr

PayAsYouGoPricePlanTriggerCondition: TypeAlias = ConditionTypeOrStr | ConditionObjectCall

PayAsYouGoPricePlanTriggerConditionDict: TypeAlias = ConditionTypeOrStr | ConditionObjectCallDict
