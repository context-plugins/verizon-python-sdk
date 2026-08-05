
# Notification Report Request

## Structure

`NotificationReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `request_type` | `str` | Required | - |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | - |
| `monitor_expiration_time` | `str` | Required | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.notification_report_request import NotificationReportRequest

notification_report_request = NotificationReportRequest(
    account_name='0242072320-00001',
    request_type='REACHABLE_FOR_DATA',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    monitor_expiration_time='2019-12-02T15:00:00-08:00Z'
)
```

