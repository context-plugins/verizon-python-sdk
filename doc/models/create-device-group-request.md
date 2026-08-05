
# Create Device Group Request

Create request for a new device group and optionally add devices to the group.

## Structure

`CreateDeviceGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The Verizon billing account that the device group will belong to. An account name is usually numeric, and must include any leading zeros. |
| `group_description` | `str` | Required | A description for the device group. |
| `group_name` | `str` | Required | The name for the new device group. This name must be unique within the specified account. |
| `devices_to_add` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to add to the device group. You can use POST /devices/actions/list to get a list of all devices in the account. |

## Example

```python
from verizon.models.create_device_group_request import CreateDeviceGroupRequest
from verizon.models.device_id import DeviceId

create_device_group_request = CreateDeviceGroupRequest(
    account_name='10001234-0001',
    group_description='Nevada tank level monitors.',
    group_name='NV tanks',
    devices_to_add=[
        DeviceId(
            id='990003420535537',
            kind='imei'
        )
    ]
)
```

