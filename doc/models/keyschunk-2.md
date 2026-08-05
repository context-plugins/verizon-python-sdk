
# Keyschunk 2

## Structure

`Keyschunk2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_percentage_50` | `bool` | Optional | - |
| `data_percentage_75` | `bool` | Optional | - |
| `data_percentage_90` | `bool` | Optional | - |
| `data_percentage_100` | `bool` | Optional | - |
| `sms_percentage_50` | `bool` | Optional | - |
| `sms_percentage_75` | `bool` | Optional | - |
| `sms_percentage_90` | `bool` | Optional | - |
| `sms_percentage_100` | `bool` | Optional | - |
| `no_of_days_b_4_promo_exp` | `int` | Optional | - |

## Example

```python
from verizon.models.keyschunk_2 import Keyschunk2

keyschunk_2 = Keyschunk2(
    data_percentage_50=False,
    data_percentage_75=False,
    data_percentage_90=False,
    data_percentage_100=False,
    sms_percentage_50=False,
    sms_percentage_75=False,
    sms_percentage_90=False,
    sms_percentage_100=True,
    no_of_days_b_4_promo_exp=5
)
```

