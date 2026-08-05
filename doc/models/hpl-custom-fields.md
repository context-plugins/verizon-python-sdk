
# Hpl Custom Fields

User assigned custom fields to use for fitering

## Structure

`HplCustomFields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | key property<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `value` | `str` | Optional | value of the key property<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |

## Example

```python
from verizon.models.hpl_custom_fields import HplCustomFields

hpl_custom_fields = HplCustomFields(
    key='key6',
    value='value8'
)
```

