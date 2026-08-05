
# Account Group Share Filter Criteria

## Structure

`AccountGroupShareFilterCriteria`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`AccountGroupShareFilter`](../../doc/models/account-group-share-filter.md) | Optional | - |
| `condition` | [`AccountGroupShareCondition`](../../doc/models/account-group-share-condition.md) | Optional | - |
| `action` | [`AccountGroupShareAction`](../../doc/models/account-group-share-action.md) | Optional | - |

## Example

```python
from verizon.models.account_group_share_action import AccountGroupShareAction
from verizon.models.account_group_share_condition import AccountGroupShareCondition
from verizon.models.account_group_share_filter import AccountGroupShareFilter
from verizon.models.account_group_share_filter_criteria import AccountGroupShareFilterCriteria
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.condition_action_enum import ConditionActionEnum
from verizon.models.notify import Notify

account_group_share_filter_criteria = AccountGroupShareFilterCriteria(
    filter_criteria=AccountGroupShareFilter(
        rate_plan_group_id=202
    ),
    condition=AccountGroupShareCondition(
        action=ConditionActionEnum.NOTIFY
    ),
    action=AccountGroupShareAction(
        notify=Notify(
            alert_type='alertType8',
            threshold=[
                Carriercode1(
                    carrier_code='carrierCode4',
                    percentage=AllowanceThreshold(
                        percentage_50=False,
                        percentage_75=False,
                        percentage_90=False,
                        percentage_100=False
                    )
                ),
                Carriercode1(
                    carrier_code='carrierCode4',
                    percentage=AllowanceThreshold(
                        percentage_50=False,
                        percentage_75=False,
                        percentage_90=False,
                        percentage_100=False
                    )
                ),
                Carriercode1(
                    carrier_code='carrierCode4',
                    percentage=AllowanceThreshold(
                        percentage_50=False,
                        percentage_75=False,
                        percentage_90=False,
                        percentage_100=False
                    )
                )
            ]
        )
    )
)
```

