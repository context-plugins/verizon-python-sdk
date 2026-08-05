
# Multi Line String

A MultiLineString is a type of geometry that represents a collection of LineString geometries.

## Structure

`MultiLineString`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Required | - |
| `coordinates` | `List[float]` | Required | **Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10`, `>= -180`, `<= 180` |

## Example

```python
from verizon.models.multi_line_string import MultiLineString
from verizon.models.type_4_enum import Type4Enum

multi_line_string = MultiLineString(
    mtype=Type4Enum.MULTILINESTRING,
    coordinates=[
        [
            [
                180,
                180
            ],
            [
                180,
                180
            ]
        ],
        [
            [
                180,
                180
            ],
            [
                180,
                180
            ]
        ]
    ]
)
```

