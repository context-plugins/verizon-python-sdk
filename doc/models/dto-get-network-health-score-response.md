
# Dto Get Network Health Score Response

The values measured are for the network

## Structure

`DtoGetNetworkHealthScoreResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `networksummary` | [`List[DtoHealthScoreMetric]`](../../doc/models/dto-health-score-metric.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `overallsummary` | [`List[DtoHealthScoreMetric]`](../../doc/models/dto-health-score-metric.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.dto_get_network_health_score_response import DtoGetNetworkHealthScoreResponse
from verizon.models.dto_health_score_metric import DtoHealthScoreMetric

dto_get_network_health_score_response = DtoGetNetworkHealthScoreResponse(
    networksummary=[
        DtoHealthScoreMetric(
            metrictype='networkscore',
            metricvalue='95'
        )
    ],
    overallsummary=[
        DtoHealthScoreMetric(
            metrictype='metrictype0',
            metricvalue='metricvalue6'
        )
    ]
)
```

