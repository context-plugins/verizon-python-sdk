
# Account Group Share Update Trigger

## Structure

`AccountGroupShareUpdateTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `data_trigger` | [`AccountGroupShareObject`](../../doc/models/account-group-share-object.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |

## Example

```python
from verizon.models.account_group_share_action import AccountGroupShareAction
from verizon.models.account_group_share_condition import AccountGroupShareCondition
from verizon.models.account_group_share_filter import AccountGroupShareFilter
from verizon.models.account_group_share_filter_criteria import AccountGroupShareFilterCriteria
from verizon.models.account_group_share_individual_1 import AccountGroupShareIndividual1
from verizon.models.account_group_share_object import AccountGroupShareObject
from verizon.models.account_group_share_update_trigger import AccountGroupShareUpdateTrigger
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.condition_action_enum import ConditionActionEnum
from verizon.models.notify import Notify
from verizon.models.trigger_category_enum import TriggerCategoryEnum

account_group_share_update_trigger = AccountGroupShareUpdateTrigger(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    account_name='0000123456-00001',
    trigger_category=TriggerCategoryEnum.DEVICEGROUPUSAGE,
    data_trigger=AccountGroupShareObject(
        account_group_share=AccountGroupShareIndividual1(
            account_group_share_individual=AccountGroupShareFilterCriteria(
                filter_criteria=AccountGroupShareFilter(
                    rate_plan_group_id=202
                ),
                condition=AccountGroupShareCondition(
                    action=ConditionActionEnum.NOTIFY
                ),
                action=AccountGroupShareAction(
                    notify=Notify(
                        alert_type='alertType8',
                        threshold=[
                            Carriercode1(
                                carrier_code='carrierCode4',
                                percentage=AllowanceThreshold(
                                    percentage_50=False,
                                    percentage_75=False,
                                    percentage_90=False,
                                    percentage_100=False
                                )
                            ),
                            Carriercode1(
                                carrier_code='carrierCode4',
                                percentage=AllowanceThreshold(
                                    percentage_50=False,
                                    percentage_75=False,
                                    percentage_90=False,
                                    percentage_100=False
                                )
                            ),
                            Carriercode1(
                                carrier_code='carrierCode4',
                                percentage=AllowanceThreshold(
                                    percentage_50=False,
                                    percentage_75=False,
                                    percentage_90=False,
                                    percentage_100=False
                                )
                            )
                        ]
                    )
                )
            )
        )
    )
)
```

