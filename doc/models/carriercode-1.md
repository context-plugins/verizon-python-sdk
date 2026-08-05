
# Carriercode 1

## Structure

`Carriercode1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_code` | `str` | Optional | - |
| `percentage` | [`AllowanceThreshold`](../../doc/models/allowance-threshold.md) | Optional | - |

## Example

```python
from verizon.models.allowance_threshold import AllowanceThreshold
from verizon.models.carriercode_1 import Carriercode1

carriercode_1 = Carriercode1(
    carrier_code='Carrier identifier code 1',
    percentage=AllowanceThreshold(
        percentage_50=False,
        percentage_75=False,
        percentage_90=False,
        percentage_100=False
    )
)
```

