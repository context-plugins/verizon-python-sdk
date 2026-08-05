
# Client Registration Request V2

Request for v2/clients/registration endpoint. It requires the Client Type, Subtype and Vendor to be defined.

## Structure

`ClientRegistrationRequestV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_type` | [`EtxClientTypeEnum`](../../doc/models/etx-client-type-enum.md) | Required | The type of the client that is to be registered. This is one of the major traffic participant groups considered in V2X communication. The system uses this value to define which topics the client will be able to publish and subscribe to.<br><br>Values:<br><br>- **Vehicle** - Vehicle with an enclosure around the passengers. (Subtypes: Motorcycle, PassengerCar, Truck, Bus, EmergencyVehicle, SchoolBus, MaintenanceVehicle)<br>- **VulnerableRoadUser** - Traffic participants without a protecting enclosure. (Subtypes: Bicycle, Pedestrian, Scooter)<br>- **TrafficLightController** - A Traffic light controller system. (Subtypes: NA)<br>- **InfrastructureSensor** - Sensors that are deployed in the infrastructure. (Subtypes: RoadSideUnit, Camera, Lidar, Radar, InductiveLoop, MagneticSensor)<br>- **OnboardSensor** - Sensors that are onboard on a vehicle(Subtypes: Camera, Lidar, Radar)<br>- **Software** - A software system or application. (Subtypes: Platform, Application, NA) |
| `client_subtype` | [`ClientSubtypeEnum`](../../doc/models/client-subtype-enum.md) | Required | The subtype or subgroup of the client type. This further specifies the client type. For example it will specify if the client is a passenger car or a truck. See the ClientType description for the supported Subtypes for each client type. |
| `vendor_id` | `str` | Required | The ID the vendor wants its devices to be registered under. E.g. Verizon, GM, Ford, etc.<br><br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |
| `device_id` | `uuid\|str` | Optional | The generated ID (UUID v4) for the device. It can be used as:<br><br>- the MQTT Client ID when connecting to the Message Exchange system<br>- a parameter when asking for the connection endpoint<br>- a parameter when finishing the device registration<br>- a parameter when unregistering the device |
| `imei` | `str` | Optional | The IMEI number of the device.<br><br>**Constraints**: *Maximum Length*: `19`, *Pattern*: `^(\d{2}-\d{6}-\d{6}-\d{1,2})$\|^(\d{15,16})$` |
| `iccid` | `str` | Optional | The ICCID number of the device.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `20`, *Pattern*: `^(89\d{17,18})$` |
| `imsi` | `str` | Optional | The IMSI number of the device.<br><br>**Constraints**: *Minimum Length*: `14`, *Maximum Length*: `15`, *Pattern*: `^\d{14,15}$` |

## Example

```python
from verizon.models.client_registration_request_v2 import ClientRegistrationRequestV2
from verizon.models.client_subtype_enum import ClientSubtypeEnum
from verizon.models.etx_client_type_enum import EtxClientTypeEnum

client_registration_request_v2 = ClientRegistrationRequestV2(
    client_type=EtxClientTypeEnum.ONBOARDSENSOR,
    client_subtype=ClientSubtypeEnum.PEDESTRIAN,
    vendor_id='VerizonETX',
    device_id='a4fcd16a-343d-4527-8203-2f46e3e4ff4b',
    imei='12-345678-901234-5',
    iccid='89345678901234567890',
    imsi='123456789012345'
)
```

