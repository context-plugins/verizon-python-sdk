
# Promo Alert 1

## Structure

`PromoAlert1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | `List[Any]` | Optional | - |
| `condition` | [`List[Keyschunk2]`](../../doc/models/keyschunk-2.md) | Optional | - |
| `enable_promo_exp` | `bool` | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.keyschunk_2 import Keyschunk2
from verizon.models.promo_alert_1 import PromoAlert1

promo_alert_1 = PromoAlert1(
    filter_criteria=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    condition=[
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        ),
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        ),
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        )
    ],
    enable_promo_exp=True
)
```

