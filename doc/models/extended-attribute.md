
# Extended Attribute

## Structure

`ExtendedAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | The key indicates if the SMS message was to the device (MtSms) or from the device (MoSms)<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `value` | `str` | Optional | The number of SMS messages found<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.extended_attribute import ExtendedAttribute

extended_attribute = ExtendedAttribute(
    key='MoSms',
    value='value2'
)
```

