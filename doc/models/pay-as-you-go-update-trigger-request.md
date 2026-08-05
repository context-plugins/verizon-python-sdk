
# Pay as You Go Update Trigger Request

## Structure

`PayAsYouGoUpdateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned UUID of the trigger |
| `trigger_name` | `str` | Optional | The user defined name of the trigger |
| `ecpd_id` | `str` | Optional | The Enterprise Customer Profile Database ID |
| `trigger_category` | [`TriggerCategoryEnum`](../../doc/models/trigger-category-enum.md) | Optional | The type of trigger being created or modified |
| `price_plan_trigger` | [`PayAsYouGoPricePlanTrigger`](../../doc/models/pay-as-you-go-price-plan-trigger.md) | Optional | - |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | - |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | A flag to indicate of the trigger is active, true, or not, false |

## Example

```python
from verizon.models.actionobject import Actionobject
from verizon.models.active_enum import ActiveEnum
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.pay_as_you_go_filter_criteria import PayAsYouGoFilterCriteria
from verizon.models.pay_as_you_go_filter_criteria_1 import PayAsYouGoFilterCriteria1
from verizon.models.pay_as_you_go_price_plan_trigger import PayAsYouGoPricePlanTrigger
from verizon.models.pay_as_you_go_update_trigger_request import PayAsYouGoUpdateTriggerRequest
from verizon.models.suspenddetailsobject import Suspenddetailsobject
from verizon.models.threshold_unit_enum import ThresholdUnitEnum
from verizon.models.trigger_category_enum import TriggerCategoryEnum

pay_as_you_go_update_trigger_request = PayAsYouGoUpdateTriggerRequest(
    trigger_id='be1b5958-ffff-eeee-gggg-b1b7618c0035',
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    trigger_category=TriggerCategoryEnum.ACCOUNTUSAGE,
    price_plan_trigger=PayAsYouGoPricePlanTrigger(
        pay_as_you_go=PayAsYouGoFilterCriteria(
            filter_criteria=PayAsYouGoFilterCriteria1(
                carrier_service_plan_code='carrierServicePlanCode4',
                account_name_list=[
                    'accountNameList7',
                    'accountNameList8'
                ]
            )
        ),
        condition=ConditionTypeEnum.AGING,
        action=Actionobject(
            suspend=False,
            suspend_details=Suspenddetailsobject(
                suspend_from_accounts=[
                    'suspendFromAccounts7'
                ],
                suspend_duration=152,
                suspend_option='suspendOption2',
                threshold=166,
                threshold_unit=ThresholdUnitEnum.GB
            ),
            change_plan=False,
            change_plan_details=ChangePlanDetails(
                to_carrier_service_plan_code='toCarrierServicePlanCode2'
            )
        )
    ),
    active=ActiveEnum.TRUE
)
```

