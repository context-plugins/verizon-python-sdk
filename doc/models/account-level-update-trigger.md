
# Account Level Update Trigger

## Structure

`AccountLevelUpdateTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger1`](../../doc/models/data-trigger-1.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_update_trigger import AccountLevelUpdateTrigger
from verizon.models.accountnames import Accountnames
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger_1 import DataTrigger1
from verizon.models.trigger_category_enum import TriggerCategoryEnum

account_level_update_trigger = AccountLevelUpdateTrigger(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    data_trigger=DataTrigger1(
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
        condition=ConditionTypeEnum.USAGEALLOWANCE,
        action=AccountLevelActionEnum.NOTIFY,
        condition_type=ConditionTypeEnum.AGING,
        comparitor=ComparitorEnum.EQ
    )
)
```

