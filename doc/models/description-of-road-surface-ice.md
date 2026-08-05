
# Description of Road Surface Ice

## Structure

`DescriptionOfRoadSurfaceIce`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ice` | [`Ice`](../../doc/models/ice.md) | Required | Indicates the surface of the roadway is ice. |

## Example

```python
from verizon.models.description_of_road_surface_ice import DescriptionOfRoadSurfaceIce
from verizon.models.ice import Ice
from verizon.models.type_12_enum import Type12Enum

description_of_road_surface_ice = DescriptionOfRoadSurfaceIce(
    ice=Ice(
        mtype=Type12Enum.SMOOTH
    )
)
```

