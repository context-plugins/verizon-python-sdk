
# Custom Fields

Custom data that can be included using key-value pairs.

## Structure

`CustomFields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | The key for an extended attribute. |
| `value` | `str` | Required | The value of an extended attribute. |

## Example

```python
from verizon.models.custom_fields import CustomFields

custom_fields = CustomFields(
    key='CustomField2',
    value='SuperVend'
)
```

