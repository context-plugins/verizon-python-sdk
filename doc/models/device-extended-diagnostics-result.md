
# Device Extended Diagnostics Result

Result for a request to obtain device extended diagnostics.

## Structure

`DeviceExtendedDiagnosticsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | [`List[DiagnosticsCategory]`](../../doc/models/diagnostics-category.md) | Optional | The response includes various types of information about the device, grouped into categories. Each category object contains the category name and a list of Extended Attribute objects as key-value pairs. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_extended_diagnostics_result import DeviceExtendedDiagnosticsResult
from verizon.models.diagnostics_category import DiagnosticsCategory

device_extended_diagnostics_result = DeviceExtendedDiagnosticsResult(
    categories=[
        DiagnosticsCategory(
            category_name='Connectivity',
            extended_attributes=[
                CustomFields(
                    key='Connected',
                    value='false'
                )
            ]
        )
    ]
)
```

