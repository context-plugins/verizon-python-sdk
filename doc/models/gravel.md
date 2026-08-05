
# Gravel

Indicates the surface of the roadway is gravel.

## Structure

`Gravel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type8Enum`](../../doc/models/type-8-enum.md) | Optional | Indicates the type of gravel. |

## Example

```python
from verizon.models.gravel import Gravel
from verizon.models.type_8_enum import Type8Enum

gravel = Gravel(
    mtype=Type8Enum.PACKEDOILED
)
```

