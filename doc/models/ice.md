
# Ice

Indicates the surface of the roadway is ice.

## Structure

`Ice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type12Enum`](../../doc/models/type-12-enum.md) | Optional | Indicates the type of ice. |

## Example

```python
from verizon.models.ice import Ice
from verizon.models.type_12_enum import Type12Enum

ice = Ice(
    mtype=Type12Enum.SMOOTH
)
```

