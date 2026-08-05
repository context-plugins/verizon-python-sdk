
# Account Level Object

## Structure

`AccountLevelObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`AccountLevelFilter`](../../doc/models/account-level-filter.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `action` | [`AccountLevelActionEnum`](../../doc/models/account-level-action-enum.md) | Optional | The action taken when trigger conditions are met |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_object import AccountLevelObject
from verizon.models.accountnames import Accountnames
from verizon.models.condition_type_enum import ConditionTypeEnum

account_level_object = AccountLevelObject(
    filter_criteria=AccountLevelFilter(
        separate_or_combined='separateOrCombined4',
        account_names=Accountnames(
            account_name_list=[
                'accountNameList7',
                'accountNameList8',
                'accountNameList9'
            ]
        )
    ),
    condition=ConditionTypeEnum.AGING,
    action=AccountLevelActionEnum.NOTIFY
)
```

