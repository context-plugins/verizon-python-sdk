
# Description of Road Surface Gravel

## Structure

`DescriptionOfRoadSurfaceGravel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gravel` | [`Gravel`](../../doc/models/gravel.md) | Required | Indicates the surface of the roadway is gravel. |

## Example

```python
from verizon.models.description_of_road_surface_gravel import DescriptionOfRoadSurfaceGravel
from verizon.models.gravel import Gravel
from verizon.models.type_8_enum import Type8Enum

description_of_road_surface_gravel = DescriptionOfRoadSurfaceGravel(
    gravel=Gravel(
        mtype=Type8Enum.PACKEDOILED
    )
)
```

