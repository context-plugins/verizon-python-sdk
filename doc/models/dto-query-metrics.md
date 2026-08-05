
# Dto Query Metrics

## Structure

`DtoQueryMetrics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Optional | The number of days in a recent period to query |

## Example

```python
from verizon.models.dto_query_metrics import DtoQueryMetrics

dto_query_metrics = DtoQueryMetrics(
    days=30
)
```

