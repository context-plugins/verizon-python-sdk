
# Road User Types Enum

The road user types:

- Vehicle: Vehicles with a metal box. Example: Car, Truck, Bus, etc.
- VulnerableRoadUser: Road users without protective housing. Example: Pedestrian, Cyclist, Motorcyclist, etc.

## Enumeration

`RoadUserTypesEnum`

## Fields

| Name |
|  --- |
| `VULNERABLEROADUSER` |
| `VEHICLE` |

## Example

```python
from verizon.models.road_user_types_enum import RoadUserTypesEnum

road_user_types = RoadUserTypesEnum.VULNERABLEROADUSER
```

