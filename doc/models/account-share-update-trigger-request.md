
# Account Share Update Trigger Request

## Structure

`AccountShareUpdateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `price_plan_trigger` | [`AccountSharePricePlanTrigger`](../../doc/models/account-share-price-plan-trigger.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | A flag to indicate of the trigger is active, true, or not, false |

## Example

```python
from verizon.models.account_share_filter_criteria import AccountShareFilterCriteria
from verizon.models.account_share_filter_criteria_1 import AccountShareFilterCriteria1
from verizon.models.account_share_price_plan_trigger import AccountSharePricePlanTrigger
from verizon.models.account_share_update_trigger_request import AccountShareUpdateTriggerRequest
from verizon.models.active_enum import ActiveEnum
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.trigger_category_enum import TriggerCategoryEnum

account_share_update_trigger_request = AccountShareUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    price_plan_trigger=AccountSharePricePlanTrigger(
        account_share=AccountShareFilterCriteria(
            filter_criteria=AccountShareFilterCriteria1(
                carrier_service_plan_code='carrierServicePlanCode4',
                account_name_list=[
                    'accountNameList7',
                    'accountNameList8'
                ]
            )
        ),
        condition=ConditionTypeEnum.AGING,
        change_plan=False,
        change_plan_details=ChangePlanDetails(
            to_carrier_service_plan_code='toCarrierServicePlanCode2'
        )
    ),
    active=ActiveEnum.TRUE
)
```

