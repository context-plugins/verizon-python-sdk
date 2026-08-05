
# Configuration List Item

The ConfigurationList's item that contains the configuration identifier, name, description and the active flag.

## Structure

`ConfigurationListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The generated ID (UUID v4) for the configuration. It has to be used when asking for changing any of the configuration parameters.<br><br>**Constraints**: *Minimum Length*: `32`, *Maximum Length*: `36`, *Pattern*: `^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?4[0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12}$` |
| `name` | `str` | Optional | Name of the configuration.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `description` | `str` | Optional | Description of the configuration.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `2048`, *Pattern*: ``^[\w\+\-!()\`\[\]{=};\"':,.\/<>?\|\s]+$`` |
| `is_active` | `bool` | Required | - |

## Example

```python
from verizon.models.configuration_list_item import ConfigurationListItem

configuration_list_item = ConfigurationListItem(
    id='a4fcd16a-343d-4527-8203-2f46e3e4ff4b',
    is_active=False,
    name='name8',
    description='description8'
)
```

