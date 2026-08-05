
# Account Level Create Trigger Request

## Structure

`AccountLevelCreateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger`](../../doc/models/data-trigger.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |
| `notification_type` | `str` | Optional | - |
| `callback` | `bool` | Optional | - |
| `email_notification` | `bool` | Optional | - |
| `notification_group_name` | `str` | Optional | - |
| `notification_frequency_factor` | `int` | Optional | - |
| `notification_frequency_interval` | `str` | Optional | - |
| `external_email_recipients` | `str` | Optional | - |
| `sms_notification` | `bool` | Optional | - |
| `sms_numbers` | List[[cellphonenumber](../../doc/models/cellphonenumber.md)] \| None | Optional | This is List of a container for any-of cases. |
| `reminder` | `bool` | Optional | - |
| `severity` | `str` | Optional | - |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | A flag to indicate of the trigger is active, true, or not, false |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_create_trigger_request import AccountLevelCreateTriggerRequest
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_object import AccountLevelObject
from verizon.models.accountnames import Accountnames
from verizon.models.active_enum import ActiveEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger import DataTrigger
from verizon.models.notificationarray import Notificationarray
from verizon.models.trigger_category_enum import TriggerCategoryEnum

account_level_create_trigger_request = AccountLevelCreateTriggerRequest(
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
    ),
    notification_type='PerEvent',
    callback=True,
    email_notification=False,
    notification_group_name='Notification Group Name (User defined)',
    notification_frequency_factor=3,
    notification_frequency_interval='Daily',
    external_email_recipients='Email addresses',
    sms_notification=True,
    reminder=True,
    severity='Notify',
    active=ActiveEnum.TRUE
)
```

