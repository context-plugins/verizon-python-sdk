
# Filtercriteria Object Call

## Structure

`FiltercriteriaObjectCall`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`FilterCriteria1`](../../doc/models/filter-criteria-1.md) | Optional | - |

## Example

```python
from verizon.models.filter_criteria_1 import FilterCriteria1
from verizon.models.filtercriteria_object_call import FiltercriteriaObjectCall

filtercriteria_object_call = FiltercriteriaObjectCall(
    filter_criteria=FilterCriteria1(
        carrier_service_plan_code='carrierServicePlanCode4',
        account_name_list=[
            'accountNameList7',
            'accountNameList8'
        ]
    )
)
```

