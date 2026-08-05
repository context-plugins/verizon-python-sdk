
# Stop Monitor Request

## Structure

`StopMonitorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.stop_monitor_request import StopMonitorRequest

stop_monitor_request = StopMonitorRequest(
    account_name='0000123456-00001',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ]
)
```

