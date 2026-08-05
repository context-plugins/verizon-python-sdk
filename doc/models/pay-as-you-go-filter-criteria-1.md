
# Pay as You Go Filter Criteria 1

## Structure

`PayAsYouGoFilterCriteria1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_service_plan_code` | `str` | Optional | - |
| `account_name_list` | `List[str]` | Optional | An array of account names |

## Example

```python
from verizon.models.pay_as_you_go_filter_criteria_1 import PayAsYouGoFilterCriteria1

pay_as_you_go_filter_criteria_1 = PayAsYouGoFilterCriteria1(
    carrier_service_plan_code='Service plan code value',
    account_name_list=[
        'accountNameList3',
        'accountNameList4'
    ]
)
```

