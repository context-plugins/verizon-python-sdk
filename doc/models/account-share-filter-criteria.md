
# Account Share Filter Criteria

## Structure

`AccountShareFilterCriteria`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`AccountShareFilterCriteria1`](../../doc/models/account-share-filter-criteria-1.md) | Optional | - |

## Example

```python
from verizon.models.account_share_filter_criteria import AccountShareFilterCriteria
from verizon.models.account_share_filter_criteria_1 import AccountShareFilterCriteria1

account_share_filter_criteria = AccountShareFilterCriteria(
    filter_criteria=AccountShareFilterCriteria1(
        carrier_service_plan_code='carrierServicePlanCode4',
        account_name_list=[
            'accountNameList7',
            'accountNameList8'
        ]
    )
)
```

