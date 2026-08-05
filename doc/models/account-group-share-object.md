
# Account Group Share Object

## Structure

`AccountGroupShareObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_group_share` | [`AccountGroupShareIndividual1`](../../doc/models/account-group-share-individual-1.md) | Optional | - |

## Example

```python
from verizon.models.account_group_share_action import AccountGroupShareAction
from verizon.models.account_group_share_condition import AccountGroupShareCondition
from verizon.models.account_group_share_filter import AccountGroupShareFilter
from verizon.models.account_group_share_filter_criteria import AccountGroupShareFilterCriteria
from verizon.models.account_group_share_individual_1 import AccountGroupShareIndividual1
from verizon.models.account_group_share_object import AccountGroupShareObject
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.condition_action_enum import ConditionActionEnum
from verizon.models.notify import Notify

account_group_share_object = AccountGroupShareObject(
    account_group_share=AccountGroupShareIndividual1(
        account_group_share_individual=AccountGroupShareFilterCriteria(
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
    )
)
```

