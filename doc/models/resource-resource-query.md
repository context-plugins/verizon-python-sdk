
# Resource Resource Query

## Structure

`ResourceResourceQuery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Devicepropertyfilter`](../../doc/models/devicepropertyfilter.md) | Optional | - |

## Example

```python
from verizon.models.devicepropertyfilter import Devicepropertyfilter
from verizon.models.devicepropertyselection import Devicepropertyselection
from verizon.models.resource_resource_query import ResourceResourceQuery

resource_resource_query = ResourceResourceQuery(
    filter=Devicepropertyfilter(
        selection=Devicepropertyselection(
            modelid='modelid0'
        ),
        querytotalcount=False
    )
)
```

