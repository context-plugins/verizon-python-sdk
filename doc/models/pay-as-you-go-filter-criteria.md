
# Pay as You Go Filter Criteria

## Structure

`PayAsYouGoFilterCriteria`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`PayAsYouGoFilterCriteria1`](../../doc/models/pay-as-you-go-filter-criteria-1.md) | Optional | - |

## Example

```python
from verizon.models.pay_as_you_go_filter_criteria import PayAsYouGoFilterCriteria
from verizon.models.pay_as_you_go_filter_criteria_1 import PayAsYouGoFilterCriteria1

pay_as_you_go_filter_criteria = PayAsYouGoFilterCriteria(
    filter_criteria=PayAsYouGoFilterCriteria1(
        carrier_service_plan_code='carrierServicePlanCode4',
        account_name_list=[
            'accountNameList7',
            'accountNameList8'
        ]
    )
)
```

