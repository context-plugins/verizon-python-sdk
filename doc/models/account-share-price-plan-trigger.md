
# Account Share Price Plan Trigger

## Structure

`AccountSharePricePlanTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_share` | [`AccountShareFilterCriteria`](../../doc/models/account-share-filter-criteria.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `change_plan` | `bool` | Optional | a flag to set if the trigger changes service plans, true, or not, false |
| `change_plan_details` | [`ChangePlanDetails`](../../doc/models/change-plan-details.md) | Optional | The service plan code to switch to |

## Example

```python
from verizon.models.account_share_filter_criteria import AccountShareFilterCriteria
from verizon.models.account_share_filter_criteria_1 import AccountShareFilterCriteria1
from verizon.models.account_share_price_plan_trigger import AccountSharePricePlanTrigger
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.condition_type_enum import ConditionTypeEnum

account_share_price_plan_trigger = AccountSharePricePlanTrigger(
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
    change_plan=True,
    change_plan_details=ChangePlanDetails(
        to_carrier_service_plan_code='toCarrierServicePlanCode2'
    )
)
```

