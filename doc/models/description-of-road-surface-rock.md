
# Description of Road Surface Rock

## Structure

`DescriptionOfRoadSurfaceRock`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rock` | [`Rock`](../../doc/models/rock.md) | Required | Indicates the surface of the roadway is rock. |

## Example

```python
from verizon.models.description_of_road_surface_rock import DescriptionOfRoadSurfaceRock
from verizon.models.rock import Rock
from verizon.models.type_11_enum import Type11Enum

description_of_road_surface_rock = DescriptionOfRoadSurfaceRock(
    rock=Rock(
        mtype=Type11Enum.CRUSHED
    )
)
```

