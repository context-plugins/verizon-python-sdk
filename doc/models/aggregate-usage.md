
# Aggregate Usage

## Structure

`AggregateUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Optional | - |
| `account_name` | `str` | Optional | The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `start_time` | `str` | Optional | The start date of the time period queried as "$datetime"<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `end_time` | `str` | Optional | The end date of the time period being queried as "$datetime"<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.aggregate_usage import AggregateUsage
from verizon.models.gio_device_id import GIODeviceId

aggregate_usage = AggregateUsage(
    device_id=GIODeviceId(
        kind='kind8',
        id='id0'
    ),
    account_name='accountName0',
    start_time='startTime2',
    end_time='endTime0'
)
```

