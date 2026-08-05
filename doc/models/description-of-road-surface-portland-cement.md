
# Description of Road Surface Portland Cement

## Structure

`DescriptionOfRoadSurfacePortlandCement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portland_cement` | [`PortlandCement`](../../doc/models/portland-cement.md) | Required | Indicates the surface of the roadway is portland cement. |

## Example

```python
from verizon.models.description_of_road_surface_portland_cement import DescriptionOfRoadSurfacePortlandCement
from verizon.models.portland_cement import PortlandCement
from verizon.models.type_6_enum import Type6Enum

description_of_road_surface_portland_cement = DescriptionOfRoadSurfacePortlandCement(
    portland_cement=PortlandCement(
        mtype=Type6Enum.TRAVELED
    )
)
```

