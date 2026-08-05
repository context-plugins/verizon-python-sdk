
# Action Object Call

## Structure

`ActionObjectCall`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Actionobject`](../../doc/models/actionobject.md) | Optional | - |

## Example

```python
from verizon.models.action_object_call import ActionObjectCall
from verizon.models.actionobject import Actionobject
from verizon.models.change_plan_details import ChangePlanDetails
from verizon.models.suspenddetailsobject import Suspenddetailsobject
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

action_object_call = ActionObjectCall(
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

