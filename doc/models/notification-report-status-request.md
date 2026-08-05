
# Notification Report Status Request

## Structure

`NotificationReportStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `device` | [`DeviceId`](../../doc/models/device-id.md) | Required | An identifier for a single device. |
| `request_type` | `str` | Required | The type of request. |
| `request_expiration_time` | `str` | Optional | The time at which the request expires. |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.notification_report_status_request import NotificationReportStatusRequest

notification_report_status_request = NotificationReportStatusRequest(
    account_name='0868924207-00001',
    device=DeviceId(
        id='990013907835573',
        kind='imei'
    ),
    request_type='requestType0',
    request_expiration_time='requestExpirationTime4'
)
```

