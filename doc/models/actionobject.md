
# Actionobject

## Structure

`Actionobject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspend` | `bool` | Optional | - |
| `suspend_details` | [`Suspenddetailsobject`](../../doc/models/suspenddetailsobject.md) | Optional | - |
| `change_plan` | `bool` | Optional | a flag to set if the trigger changes service plans, true, or not, false |
| `change_plan_details` | [`ChangePlanDetails`](../../doc/models/change-plan-details.md) | Optional | The service plan code to switch to |

## Example

```python
from verizon.models.actionobject import Actionobject
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.suspenddetailsobject import Suspenddetailsobject
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

actionobject = Actionobject(
    suspend=True,
    suspend_details=Suspenddetailsobject(
        suspend_from_accounts=[
            'suspendFromAccounts7'
        ],
        suspend_duration=152,
        suspend_option='suspendOption2',
        threshold=166,
        threshold_unit=ThresholdUnitEnum.GB
    ),
    change_plan=True,
    change_plan_details=ChangePlanDetails(
        to_carrier_service_plan_code='toCarrierServicePlanCode2'
    )
)
```

