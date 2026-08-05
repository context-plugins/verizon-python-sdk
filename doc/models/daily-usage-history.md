
# Daily Usage History

## Structure

`DailyUsageHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bytes_used` | `str` | Optional | the total data usage recorded in Bytes<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{1,32}$` |
| `extended_attributes` | [`List[ExtendedAttribute]`](../../doc/models/extended-attribute.md) | Optional | - |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `sms_used` | `str` | Optional | The total number of SMS messages from and to the device<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{1,32}$` |
| `source` | `str` | Optional | Where the collected data is being gathered from<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `timestamp` | `str` | Optional | Timestamp of when the retrieved record was completed ($datetime)<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.daily_usage_history import DailyUsageHistory
from verizon.models.extended_attribute import ExtendedAttribute

daily_usage_history = DailyUsageHistory(
    bytes_used='123456',
    extended_attributes=[
        ExtendedAttribute(
            key='key8',
            value='value0'
        ),
        ExtendedAttribute(
            key='key8',
            value='value0'
        )
    ],
    service_plan='servicePlan4',
    sms_used='5',
    source='source2'
)
```

