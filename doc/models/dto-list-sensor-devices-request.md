
# Dto List Sensor Devices Request

## Structure

`DtoListSensorDevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `filter` | [`DtoFilter`](../../doc/models/dto-filter.md) | Optional | - |
| `resourceidentifier` | [`DtoDeviceResourceIdentifier`](../../doc/models/dto-device-resource-identifier.md) | Optional | Device identifiers, one or more are required |

## Example

```python
from verizon.models.dto_device_resource_identifier import DtoDeviceResourceIdentifier
from verizon.models.dto_filter import DtoFilter
from verizon.models.dto_list_sensor_devices_request import DtoListSensorDevicesRequest

dto_list_sensor_devices_request = DtoListSensorDevicesRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='$expand0',
        limitnumber=100,
        nopagination=False,
        page='$page0',
        pagenumber=64
    ),
    resourceidentifier=DtoDeviceResourceIdentifier(
        deveui='deveui2',
        deviceid='deviceid6',
        esn=86,
        iccid='iccid0',
        imei=2
    )
)
```

