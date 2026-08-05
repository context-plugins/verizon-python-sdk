
# Daily Usage

## Structure

`DailyUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Optional | - |
| `earliest` | `str` | Optional | The start date of the time period queried as "$datetime"<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `latest` | `str` | Optional | The end date of the time period being queried as "$datetime"<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.daily_usage import DailyUsage
from verizon.models.gio_device_id import GIODeviceId

daily_usage = DailyUsage(
    device_id=GIODeviceId(
        kind='kind8',
        id='id0'
    ),
    earliest='earliest6',
    latest='latest2'
)
```

