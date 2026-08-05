
# Description of Road Surface Snow

## Structure

`DescriptionOfRoadSurfaceSnow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `snow` | [`Snow`](../../doc/models/snow.md) | Required | Indicates the surface of the roadway is snow. |

## Example

```python
from verizon.models.description_of_road_surface_snow import DescriptionOfRoadSurfaceSnow
from verizon.models.snow import Snow
from verizon.models.type_13_enum import Type13Enum

description_of_road_surface_snow = DescriptionOfRoadSurfaceSnow(
    snow=Snow(
        mtype=Type13Enum.PACKED
    )
)
```

