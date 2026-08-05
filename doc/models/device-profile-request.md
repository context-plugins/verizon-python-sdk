
# Device Profile Request

## Structure

`DeviceProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[GIODeviceList]`](../../doc/models/gio-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9\-]{3,32}$` |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |

## Example

```python
from verizon.models.device_profile_request import DeviceProfileRequest
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.gio_device_list import GIODeviceList

device_profile_request = DeviceProfileRequest(
    devices=[
        GIODeviceList(
            device_ids=[
                GIODeviceId(
                    kind='kind8',
                    id='id0'
                )
            ]
        ),
        GIODeviceList(
            device_ids=[
                GIODeviceId(
                    kind='kind8',
                    id='id0'
                )
            ]
        ),
        GIODeviceList(
            device_ids=[
                GIODeviceId(
                    kind='kind8',
                    id='id0'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    service_plan='service plan name'
)
```

