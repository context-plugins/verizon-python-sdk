
# Snow

Indicates the surface of the roadway is snow.

## Structure

`Snow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type13Enum`](../../doc/models/type-13-enum.md) | Optional | Indicates the type of snow. |

## Example

```python
from verizon.models.snow import Snow
from verizon.models.type_13_enum import Type13Enum

snow = Snow(
    mtype=Type13Enum.PACKED
)
```

