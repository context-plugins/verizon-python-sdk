
# Cinders

Indicates the surface of the roadway is cinders.

## Structure

`Cinders`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type10Enum`](../../doc/models/type-10-enum.md) | Optional | Indicates the type of cinders. |

## Example

```python
from verizon.models.cinders import Cinders
from verizon.models.type_10_enum import Type10Enum

cinders = Cinders(
    mtype=Type10Enum.PACKED
)
```

