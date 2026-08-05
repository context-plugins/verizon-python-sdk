
# Rock

Indicates the surface of the roadway is rock.

## Structure

`Rock`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type11Enum`](../../doc/models/type-11-enum.md) | Optional | Indicates the type of rock. |

## Example

```python
from verizon.models.rock import Rock
from verizon.models.type_11_enum import Type11Enum

rock = Rock(
    mtype=Type11Enum.CRUSHED
)
```

