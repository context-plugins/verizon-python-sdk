
# SMS Trigger Request

## Structure

`SMSTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comparator` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `sms_type` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `threshold` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |

## Example

```python
from verizon.models.sms_trigger_request import SMSTriggerRequest

sms_trigger_request = SMSTriggerRequest(
    comparator='comparator4',
    sms_type='smsType2',
    threshold=56
)
```

