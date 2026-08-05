
# Filtercriteria 2

## Structure

`Filtercriteria2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | `List[Any]` | Optional | - |

## Example

```python
import jsonpickle

from verizon.models.filtercriteria_2 import Filtercriteria2

filtercriteria_2 = Filtercriteria2(
    filter_criteria=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

