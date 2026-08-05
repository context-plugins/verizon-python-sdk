
# Account Level Create Trigger

## Structure

`AccountLevelCreateTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger`](../../doc/models/data-trigger.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_create_trigger import AccountLevelCreateTrigger
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_object import AccountLevelObject
from verizon.models.accountnames import Accountnames
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger import DataTrigger
from verizon.models.notificationarray import Notificationarray
from verizon.models.trigger_category_enum import TriggerCategoryEnum

account_level_create_trigger = AccountLevelCreateTrigger(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.DEVICEGROUPUSAGE,
    data_trigger=DataTrigger(
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
    ),
    notification=Notificationarray(
        notification_type='notificationType8',
        callback=False,
        email_notification=False,
        notification_group_name='notificationGroupName6',
        notification_frequency_factor=22
    )
)
```

