
# Polygon

A Polygon is a type of geometry that represents a collection of points that form a closed ring.

NOTE: This API only supports a single polygon in the Polygon geometry, so holes cannot be defines at this point. Support for hole will be added in future releases.

## Structure

`Polygon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Required | - |
| `coordinates` | `List[float]` | Required | **Constraints**: *Minimum Items*: `1`, *Maximum Items*: `1`, `>= -180`, `<= 180` |

## Example

```python
from verizon.models.polygon import Polygon
from verizon.models.type_3_enum import Type3Enum

polygon = Polygon(
    mtype=Type3Enum.POLYGON,
    coordinates=[
        [
            [
                41.65,
                41.66
            ],
            [
                41.65,
                41.66
            ]
        ],
        [
            [
                41.65,
                41.66
            ],
            [
                41.65,
                41.66
            ]
        ]
    ]
)
```

