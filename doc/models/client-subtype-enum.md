
# Client Subtype Enum

The subtype or subgroup of the client type. This further specifies the client type. For example it will specify if the client is a passenger car or a truck. See the ClientType description for the supported Subtypes for each client type.

## Enumeration

`ClientSubtypeEnum`

## Fields

| Name |
|  --- |
| `PASSENGERCAR` |
| `TRUCK` |
| `BUS` |
| `EMERGENCYVEHICLE` |
| `SCHOOLBUS` |
| `MAINTENANCEVEHICLE` |
| `PEDESTRIAN` |
| `BICYCLE` |
| `SCOOTER` |
| `MOTORCYCLE` |
| `ROADSIDEUNIT` |
| `CAMERA` |
| `LIDAR` |
| `RADAR` |
| `INDUCTIVELOOP` |
| `MAGNETICSENSOR` |
| `PLATFORM` |
| `APPLICATION` |
| `NA` |

## Example

```python
from verizon.models.client_subtype_enum import ClientSubtypeEnum

client_subtype = ClientSubtypeEnum.SCOOTER
```

