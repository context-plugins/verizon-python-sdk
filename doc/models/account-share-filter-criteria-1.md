
# Account Share Filter Criteria 1

## Structure

`AccountShareFilterCriteria1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_service_plan_code` | `str` | Optional | - |
| `account_name_list` | `List[str]` | Optional | An array of account names |

## Example

```python
from verizon.models.account_share_filter_criteria_1 import AccountShareFilterCriteria1

account_share_filter_criteria_1 = AccountShareFilterCriteria1(
    carrier_service_plan_code='Service plan code value',
    account_name_list=[
        'accountNameList3',
        'accountNameList4',
        'accountNameList5'
    ]
)
```

