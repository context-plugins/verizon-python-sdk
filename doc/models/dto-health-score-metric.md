
# Dto Health Score Metric

## Structure

`DtoHealthScoreMetric`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metrictype` | `str` | Optional | The type of measurement and can be overallscore, networkscore, gatewayscore, sensorscore, networkstatus, averagesignalstrength or networkavailabilitylast30 |
| `metricvalue` | `str` | Optional | the value of the `metrictype` as a percentage |

## Example

```python
from verizon.models.dto_health_score_metric import DtoHealthScoreMetric

dto_health_score_metric = DtoHealthScoreMetric(
    metrictype='overallscore',
    metricvalue='95'
)
```

