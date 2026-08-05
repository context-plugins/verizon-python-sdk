
# Line String

A LineString is a type of geometry that represents a collection of points that are connected by line segments.

## Structure

`LineString`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Required | - |
| `coordinates` | `List[float]` | Required | **Constraints**: *Minimum Items*: `2`, *Maximum Items*: `63`, `>= -180`, `<= 180` |

## Example

```python
from verizon.models.line_string import LineString
from verizon.models.type_2_enum import Type2Enum

line_string = LineString(
    mtype=Type2Enum.LINESTRING,
    coordinates=[
        [
            180,
            180,
            180
        ],
        [
            180,
            180,
            180
        ],
        [
            180,
            180,
            180
        ]
    ]
)
```

