
# Pay as You Go Price Plan Trigger

## Structure

`PayAsYouGoPricePlanTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pay_as_you_go` | [`PayAsYouGoFilterCriteria`](../../doc/models/pay-as-you-go-filter-criteria.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `action` | [`Actionobject`](../../doc/models/actionobject.md) | Optional | - |

## Example

```python
from verizon.models.actionobject import Actionobject
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.pay_as_you_go_filter_criteria import PayAsYouGoFilterCriteria
from verizon.models.pay_as_you_go_filter_criteria_1 import PayAsYouGoFilterCriteria1
from verizon.models.pay_as_you_go_price_plan_trigger import PayAsYouGoPricePlanTrigger
from verizon.models.suspenddetailsobject import Suspenddetailsobject
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

pay_as_you_go_price_plan_trigger = PayAsYouGoPricePlanTrigger(
    pay_as_you_go=PayAsYouGoFilterCriteria(
        filter_criteria=PayAsYouGoFilterCriteria1(
            carrier_service_plan_code='carrierServicePlanCode4',
            account_name_list=[
                'accountNameList7',
                'accountNameList8'
            ]
        )
    ),
    condition=ConditionTypeEnum.USAGEALLOWANCE,
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
)
```

