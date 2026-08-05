
# Condition

## Structure

`Condition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `condition` | [`List[Keyschunk2]`](../../doc/models/keyschunk-2.md) | Optional | - |

## Example

```python
from verizon.models.condition import Condition
from verizon.models.keyschunk_2 import Keyschunk2

condition = Condition(
    condition=[
        Keyschunk2(
            data_percentage_50=False,
            data_percentage_75=False,
            data_percentage_90=False,
            data_percentage_100=False,
            sms_percentage_50=False
        )
    ]
)
```

