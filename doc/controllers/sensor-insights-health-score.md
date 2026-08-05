# Sensor Insights Health Score

```python
sensor_insights_health_score_controller = client.sensor_insights_health_score
```

## Class Name

`SensorInsightsHealthScoreController`

## Methods

* [Sensor Insights Health Score Summary](../../doc/controllers/sensor-insights-health-score.md#sensor-insights-health-score-summary)
* [Sensor Insights Get Network Health Score Response](../../doc/controllers/sensor-insights-health-score.md#sensor-insights-get-network-health-score-response)


# Sensor Insights Health Score Summary

```python
def sensor_insights_health_score_summary(self)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Response Type

**200**: Get health score summary

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoHealthScoreSummary`](../../doc/models/dto-health-score-summary.md).

## Example Usage

```python
result = sensor_insights_health_score_controller.sensor_insights_health_score_summary()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |


# Sensor Insights Get Network Health Score Response

```python
def sensor_insights_get_network_health_score_response(self)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Response Type

**200**: Get a network health score

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoGetNetworkHealthScoreResponse`](../../doc/models/dto-get-network-health-score-response.md).

## Example Usage

```python
result = sensor_insights_health_score_controller.sensor_insights_get_network_health_score_response()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |

