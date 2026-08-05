
# Account Group Share Action

## Structure

`AccountGroupShareAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notify` | [`Notify`](../../doc/models/notify.md) | Optional | - |

## Example

```python
from verizon.models.account_group_share_action import AccountGroupShareAction
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.notify import Notify

account_group_share_action = AccountGroupShareAction(
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
```

