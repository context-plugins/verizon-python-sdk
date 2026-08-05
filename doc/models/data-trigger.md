
# Data Trigger

## Structure

`DataTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_level` | [`AccountLevelObject`](../../doc/models/account-level-object.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_object import AccountLevelObject
from verizon.models.accountnames import Accountnames
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger import DataTrigger

data_trigger = DataTrigger(
    account_level=AccountLevelObject(
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
        condition=ConditionTypeEnum.INDIVIDUAL,
        action=AccountLevelActionEnum.SUSPEND
    )
)
```

