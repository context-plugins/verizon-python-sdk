# Device Reports

```python
device_reports_controller = client.device_reports
```

## Class Name

`DeviceReportsController`

## Methods

* [Calculate Aggregated Report Synchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-synchronous)
* [Calculate Aggregated Report Asynchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-asynchronous)
* [Get Sessions Report](../../doc/controllers/device-reports.md#get-sessions-report)


# Calculate Aggregated Report Synchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

```python
def calculate_aggregated_report_synchronous(self,
                                           body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated report request. |

## Response Type

**200**: A successful response shows session and usage details for up to 10 devices.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregateSessionReport`](../../doc/models/aggregate-session-report.md).

## Example Usage

```python
body = AggregateSessionReportRequest(
    account_number='0000123456-00001',
    imei=[
        '15-digit IMEI'
    ],
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    device_group='string',
    data_plan='string',
    no_session_flag=False
)

result = device_reports_controller.calculate_aggregated_report_synchronous(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Calculate Aggregated Report Asynchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive an asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

```python
def calculate_aggregated_report_asynchronous(self,
                                            body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated session report request. |

## Response Type

**200**: A successful response shows the request is queued with a unique `txid` to identify the report data with.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AggregatedReportCallbackResult`](../../doc/models/aggregated-report-callback-result.md).

## Example Usage

```python
body = AggregateSessionReportRequest(
    account_number='0000123456-00001',
    imei=[
        '15-digit IMEI'
    ],
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    device_group='string',
    data_plan='string',
    no_session_flag=False
)

result = device_reports_controller.calculate_aggregated_report_asynchronous(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "txid": "60c07fff-eeee-ffff-gggg-75e6a7c238f6",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Get Sessions Report

Detailed report of session duration and number of bytes transferred per day.

```python
def get_sessions_report(self,
                       body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SessionReportRequest`](../../doc/models/session-report-request.md) | Body, Required | Request for sessions report. |

## Response Type

**200**: A successful response includes the session information for an individual device.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SessionReport`](../../doc/models/session-report.md).

## Example Usage

```python
body = SessionReportRequest(
    account_number='0000123456-00001',
    imei='15-digit IMEI',
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    duration_low=0,
    duration_high=0
)

result = device_reports_controller.get_sessions_report(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "The 10-digit ID of the device",
  "txid": "60c07fff-eeee-ffff-gggg-75e6a7c238f6",
  "sessions": [
    {
      "startTime": "Start date of session. ISO 8601 format.",
      "endTime": "End date of session. ISO 8601 format.",
      "numBytes": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |

