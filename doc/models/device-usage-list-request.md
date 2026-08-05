
# Device Usage List Request

Request to return the daily network data usage of a single device during a specified time period.

## Structure

`DeviceUsageListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `earliest` | `str` | Required | The earliest date for which you want usage data. |
| `latest` | `str` | Required | The last date for which you want usage data. |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | An identifier for a single device. |
| `label` | [`Label`](../../doc/models/label.md) | Optional | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_usage_list_request import DeviceUsageListRequest
from verizon.models.label import Label

device_usage_list_request = DeviceUsageListRequest(
    earliest='2018-03-20T00:00:01Z',
    latest='2020-12-31T00:00:01Z',
    device_id=DeviceId(
        id=None,
        kind=None
    ),
    label=Label(
        name='name0',
        value='value2'
    )
)
```

