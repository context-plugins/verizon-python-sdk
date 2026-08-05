
# Multi Polygon

A MultiPolygon is a type of geometry that represents a collection of Polygon geometries.

## Structure

`MultiPolygon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Required | - |
| `coordinates` | `List[float]` | Required | **Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10`, `>= -180`, `<= 180` |

## Example

```python
from verizon.models.multi_polygon import MultiPolygon
from verizon.models.type_5_enum import Type5Enum

multi_polygon = MultiPolygon(
    mtype=Type5Enum.MULTIPOLYGON,
    coordinates=[
        [
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ]
        ],
        [
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ]
        ],
        [
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ],
            [
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ],
                [
                    28.83,
                    28.82,
                    28.81
                ]
            ]
        ]
    ]
)
```

