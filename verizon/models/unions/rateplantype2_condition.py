from __future__ import annotations

from typing import TypeAlias

from ..condition_object_call import ConditionObjectCall, ConditionObjectCallDict
from ..enums.condition_type import ConditionTypeOrStr

Rateplantype2Condition: TypeAlias = ConditionTypeOrStr | ConditionObjectCall

Rateplantype2ConditionDict: TypeAlias = ConditionTypeOrStr | ConditionObjectCallDict
