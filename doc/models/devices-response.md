
# Devices Response

Device information containing ID, type classification, and associated MEC IDs

## Structure

`DevicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `uuid\|str` | Required | The generated ID (UUID v4) for the device. It can be used as:<br><br>- the MQTT Client ID when connecting to the Message Exchange system<br>- a parameter when asking for the connection endpoint<br>- a parameter when finishing the device registration<br>- a parameter when unregistering the device |
| `client_type` | [`EtxClientTypeEnum`](../../doc/models/etx-client-type-enum.md) | Required | The type of the client that is to be registered. This is one of the major traffic participant groups considered in V2X communication. The system uses this value to define which topics the client will be able to publish and subscribe to.<br><br>Values:<br><br>- **Vehicle** - Vehicle with an enclosure around the passengers. (Subtypes: Motorcycle, PassengerCar, Truck, Bus, EmergencyVehicle, SchoolBus, MaintenanceVehicle)<br>- **VulnerableRoadUser** - Traffic participants without a protecting enclosure. (Subtypes: Bicycle, Pedestrian, Scooter)<br>- **TrafficLightController** - A Traffic light controller system. (Subtypes: NA)<br>- **InfrastructureSensor** - Sensors that are deployed in the infrastructure. (Subtypes: RoadSideUnit, Camera, Lidar, Radar, InductiveLoop, MagneticSensor)<br>- **OnboardSensor** - Sensors that are onboard on a vehicle(Subtypes: Camera, Lidar, Radar)<br>- **Software** - A software system or application. (Subtypes: Platform, Application, NA) |
| `client_subtype` | [`ClientSubtypeEnum`](../../doc/models/client-subtype-enum.md) | Required | The subtype or subgroup of the client type. This further specifies the client type. For example it will specify if the client is a passenger car or a truck. See the ClientType description for the supported Subtypes for each client type. |
| `mec_ids` | `List[str]` | Required | **Constraints**: *Minimum Items*: `0`, *Maximum Items*: `10`, *Maximum Length*: `128`, *Pattern*: `^[a-z0-9\-]+$` |

## Example

```python
from verizon.models.client_subtype_enum import ClientSubtypeEnum
from verizon.models.devices_response import DevicesResponse
from verizon.models.etx_client_type_enum import EtxClientTypeEnum

devices_response = DevicesResponse(
    device_id='a4fcd16a-343d-4527-8203-2f46e3e4ff4b',
    client_type=EtxClientTypeEnum.ONBOARDSENSOR,
    client_subtype=ClientSubtypeEnum.MOTORCYCLE,
    mec_ids=[
        'MecIds3'
    ]
)
```

