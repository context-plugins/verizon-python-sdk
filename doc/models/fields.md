
# Fields

List of fields affected by the event.

## Structure

`Fields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | [`Configuration`](../../doc/models/configuration.md) | Optional | List of the field names and values to set. |

## Example

```python
from verizon.models.configuration import Configuration
from verizon.models.fields import Fields

fields = Fields(
    configuration=Configuration(
        frequency='Low'
    )
)
```

