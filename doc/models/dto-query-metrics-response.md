
# Dto Query Metrics Response

## Structure

`DtoQueryMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `critical` | `int` | Optional | The number of critical alerts in the queried time period |
| `major` | `int` | Optional | The number of major alerts in the queried time period |
| `minor` | `int` | Optional | The number of minor alerts in the queried time period |
| `noalert` | `int` | Optional | The number of sensor reports containing no  alerts in the queried time period |
| `total` | `int` | Optional | The total number of alerts in the queried time period |
| `deltacritical` | `int` | Optional | The change in the number of critical alerts in the queried time period |
| `deltamajor` | `int` | Optional | The change in the number of major alerts in the queried time period |
| `deltaminor` | `int` | Optional | The change in the number of minor alerts in the queried time period |
| `deltanoalert` | `int` | Optional | The change in the number of sensor reports containing no alerts in the queried time period |

## Example

```python
from verizon.models.dto_query_metrics_response import DtoQueryMetricsResponse

dto_query_metrics_response = DtoQueryMetricsResponse(
    critical=0,
    major=0,
    minor=0,
    noalert=1,
    total=1,
    deltacritical=-3,
    deltamajor=-1,
    deltaminor=0,
    deltanoalert=-15
)
```

