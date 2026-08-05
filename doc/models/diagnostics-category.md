
# Diagnostics Category

Various types of information about the device, grouped into categories. Each category object contains the category name and a list of Extended Attribute objects as key-value pairs.

## Structure

`DiagnosticsCategory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_name` | `str` | Optional | The name of the category. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | A list of Extended Attribute objects as key-value pairs. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.diagnostics_category import DiagnosticsCategory

diagnostics_category = DiagnosticsCategory(
    category_name='Connectivity',
    extended_attributes=[
        CustomFields(
            key='Connected',
            value='false'
        )
    ]
)
```

