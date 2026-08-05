
# Extended Attributes

Additional properties associated with data.

## Structure

`ExtendedAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | - |
| `value` | `str` | Optional | - |

## Example

```python
from verizon.models.extended_attributes import ExtendedAttributes

extended_attributes = ExtendedAttributes(
    key='key6',
    value='value8'
)
```

