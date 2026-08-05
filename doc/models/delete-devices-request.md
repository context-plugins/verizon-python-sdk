
# Delete Devices Request

Request to delete a device request.

## Structure

`DeleteDevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices_to_delete` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | A list of up to 100 devices that you want to delete, specified by device identifier. You only need to provide one identifier per device. |
| `account_name` | `str` | Optional | The Verizon billing account that the device group belongs to. An account name is usually numeric, and must include any leading zeros. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.delete_devices_request import DeleteDevicesRequest
from verizon.models.device_id import DeviceId

delete_devices_request = DeleteDevicesRequest(
    devices_to_delete=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='09005470263',
                    kind='esn'
                )
            ],
            ipaddress='ipAddress8'
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='85000022411113460014',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress8'
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='85000022412313460016',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress8'
        )
    ],
    account_name='accountName6'
)
```

