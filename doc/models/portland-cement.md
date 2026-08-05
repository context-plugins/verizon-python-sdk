
# Portland Cement

Indicates the surface of the roadway is portland cement.

## Structure

`PortlandCement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | Indicates the type of portland cement.<br><br>**Default**: `"traveled"` |

## Example

```python
from verizon.models.portland_cement import PortlandCement
from verizon.models.type_6_enum import Type6Enum

portland_cement = PortlandCement(
    mtype=Type6Enum.TRAVELED
)
```

