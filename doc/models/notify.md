
# Notify

## Structure

`Notify`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alert_type` | `str` | Optional | - |
| `threshold` | List[[carriercode1](../../doc/models/carriercode-1.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example

```python
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1
from verizon.models.notify import Notify

notify = Notify(
    alert_type='individualpriceplan',
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
```

