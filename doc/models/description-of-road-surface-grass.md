
# Description of Road Surface Grass

## Structure

`DescriptionOfRoadSurfaceGrass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grass` | [`Grass`](../../doc/models/grass.md) | Required | Indicates the surface of the roadway is grass. |

## Example

```python
from verizon.models.description_of_road_surface_grass import DescriptionOfRoadSurfaceGrass
from verizon.models.grass import Grass
from verizon.models.type_9_enum import Type9Enum

description_of_road_surface_grass = DescriptionOfRoadSurfaceGrass(
    grass=Grass(
        mtype=Type9Enum.LESSTHAN30MPH
    )
)
```

