# Device Monitoring

```python
device_monitoring_controller = client.device_monitoring
```

## Class Name

`DeviceMonitoringController`

## Methods

* [Device Reachability](../../doc/controllers/device-monitoring.md#device-reachability)
* [Stop Device Reachability](../../doc/controllers/device-monitoring.md#stop-device-reachability)


# Device Reachability

```python
def device_reachability(self,
                       body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotificationReportRequest`](../../doc/models/notification-report-request.md) | Body, Required | Create Reachability Report Request |

## Response Type

**200**: Request ID

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RequestResponse`](../../doc/models/request-response.md).

## Example Usage

```python
body = NotificationReportRequest(
    account_name='0000123456-00001',
    request_type='REACHABLE_FOR_DATA',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                ),
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        )
    ],
    monitor_expiration_time='2019-12-02T15:00:00-08:00Z'
)

result = device_monitoring_controller.device_reachability(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Stop Device Reachability

```python
def stop_device_reachability(self,
                            stopreachabilitypayload)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stopreachabilitypayload` | [`StopMonitorRequest`](../../doc/models/stop-monitor-request.md) | Query, Required | Payload for the Stop Device Reachability monitors request. |

## Response Type

**200**: Request ID

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RequestResponse`](../../doc/models/request-response.md).

## Example Usage

```python
stopreachabilitypayload = StopMonitorRequest(
    account_name='0000123456-00001',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='1+ 10-digit phone number',
                    kind='msisdn'
                )
            ]
        )
    ]
)

result = device_monitoring_controller.stop_device_reachability(stopreachabilitypayload)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

