
# V2 Triggers Request

## Structure

`V2TriggersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger4`](../../doc/models/data-trigger-4.md) | Optional | - |
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
| `filter_criteria` | [`AccountLevelFilter`](../../doc/models/account-level-filter.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `action` | [`AccountLevelActionEnum`](../../doc/models/account-level-action-enum.md) | Optional | The action taken when trigger conditions are met |
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes |
| `price_plan_trigger` | [`PricePlanTrigger1`](../../doc/models/price-plan-trigger-1.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.account_level_object import AccountLevelObject
from verizon.models.accountnames import Accountnames
from verizon.models.active_enum import ActiveEnum
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger_4 import DataTrigger4
from verizon.models.device_group_filter import DeviceGroupFilter
from verizon.models.device_group_filter_criteria import DeviceGroupFilterCriteria
from verizon.models.notificationarray import Notificationarray
from verizon.models.trigger_category_enum import TriggerCategoryEnum
from verizon.models.v2_triggers_request import V2TriggersRequest

v2_triggers_request = V2TriggersRequest(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    data_trigger=DataTrigger4(
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
        ),
        device_group=DeviceGroupFilterCriteria(
            filter_criteria=DeviceGroupFilter(
                device_group_name='deviceGroupName4',
                individual_or_combined='IndividualOrCombined4',
                account_name='accountName0'
            )
        ),
        condition_type=ConditionTypeEnum.AGING,
        comparitor=ComparitorEnum.EQ,
        threshold=222
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
    active=ActiveEnum.TRUE,
    action=AccountLevelActionEnum.NOTIFY,
    account_name='0000123456-00001'
)
```

