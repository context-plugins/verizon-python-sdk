
# Filter Criteria 1

## Structure

`FilterCriteria1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_service_plan_code` | `str` | Optional | - |
| `account_name_list` | `List[str]` | Optional | An array of account names |

## Example

```python
from verizon.models.filter_criteria_1 import FilterCriteria1

filter_criteria_1 = FilterCriteria1(
    carrier_service_plan_code='Service plan code value',
    account_name_list=[
        'accountNameList9'
    ]
)
```

