
# Description of Road Surface Cinders

## Structure

`DescriptionOfRoadSurfaceCinders`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cinders` | [`Cinders`](../../doc/models/cinders.md) | Required | Indicates the surface of the roadway is cinders. |

## Example

```python
from verizon.models.cinders import Cinders
from verizon.models.description_of_road_surface_cinders import DescriptionOfRoadSurfaceCinders
from verizon.models.type_10_enum import Type10Enum

description_of_road_surface_cinders = DescriptionOfRoadSurfaceCinders(
    cinders=Cinders(
        mtype=Type10Enum.PACKED
    )
)
```

