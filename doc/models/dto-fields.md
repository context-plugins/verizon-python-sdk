
# Dto Fields

Fields to return needed by search

## Structure

`DtoFields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_prop_1` | `str` | Optional | - |
| `additional_prop_2` | `str` | Optional | - |
| `additional_prop_3` | `str` | Optional | - |

## Example

```python
from verizon.models.dto_fields import DtoFields

dto_fields = DtoFields(
    additional_prop_1='string',
    additional_prop_2='string',
    additional_prop_3='string'
)
```

