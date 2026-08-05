
# Grass

Indicates the surface of the roadway is grass.

## Structure

`Grass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type9Enum`](../../doc/models/type-9-enum.md) | Optional | Indicates the surface of the roadway is grass with low speed limit. |

## Example

```python
from verizon.models.grass import Grass
from verizon.models.type_9_enum import Type9Enum

grass = Grass(
    mtype=Type9Enum.LESSTHAN30MPH
)
```

