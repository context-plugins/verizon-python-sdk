
# V2 Triggers Request 1

## Structure

`V2TriggersRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`DataTrigger5`](../../doc/models/data-trigger-5.md) | Optional | - |
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
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes |
| `price_plan_trigger` | [`PricePlanTrigger2`](../../doc/models/price-plan-trigger-2.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.accountnames import Accountnames
from verizon.models.active_enum import ActiveEnum
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger_5 import DataTrigger5
from verizon.models.trigger_category_enum import TriggerCategoryEnum
from verizon.models.v2_triggers_request_1 import V2TriggersRequest1

v2_triggers_request_1 = V2TriggersRequest1(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.PRICEPLANDATAUSAGE,
    data_trigger=DataTrigger5(
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
    account_name='0000123456-00001'
)
```

