
# Dto Health Score Summary

The values measured are for sensors and gateways

## Structure

`DtoHealthScoreSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `overallsummary` | [`List[DtoHealthScoreMetric]`](../../doc/models/dto-health-score-metric.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.dto_health_score_metric import DtoHealthScoreMetric
from verizon.models.dto_health_score_summary import DtoHealthScoreSummary

dto_health_score_summary = DtoHealthScoreSummary(
    overallsummary=[
        DtoHealthScoreMetric(
            metrictype='metrictype0',
            metricvalue='metricvalue6'
        ),
        DtoHealthScoreMetric(
            metrictype='metrictype0',
            metricvalue='metricvalue6'
        )
    ]
)
```

