
# SMS Number

Notification SMS details.

## Structure

`SMSNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier` | `str` | Optional | - |
| `number` | `str` | Optional | - |

## Example

```python
from verizon.models.sms_number import SMSNumber

sms_number = SMSNumber(
    carrier='US Cellular',
    number='9299280711'
)
```

