
# Get Device Statuses Responseforplanner

## Structure

`GetDeviceStatusesResponseforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `request_id` | `str` | Optional | - |
| `device_status_list` | [`List[DeviceStatusItemforplanner]`](../../doc/models/device-status-itemforplanner.md) | Optional | - |

## Example

```python
from verizon.models.device_idforplanner import DeviceIdforplanner
from verizon.models.device_status_itemforplanner import DeviceStatusItemforplanner
from verizon.models.get_device_statuses_responseforplanner import GetDeviceStatusesResponseforplanner

get_device_statuses_responseforplanner = GetDeviceStatusesResponseforplanner(
    account_number='0000123456-00001',
    request_id='requestId2',
    device_status_list=[
        DeviceStatusItemforplanner(
            device_ids=[
                DeviceIdforplanner(
                    kind='kind8',
                    id='id0'
                )
            ],
            status='status6',
            reason='reason2'
        ),
        DeviceStatusItemforplanner(
            device_ids=[
                DeviceIdforplanner(
                    kind='kind8',
                    id='id0'
                )
            ],
            status='status6',
            reason='reason2'
        )
    ]
)
```

