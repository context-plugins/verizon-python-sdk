# Intelligence Service Controller

```python
intelligence_service_controller = client.intelligence_service_controller
```

## Class Name

`IntelligenceServiceController`

## Methods

* [Set Connection Planner](../../doc/controllers/intelligence-service-controller.md#set-connection-planner)
* [Status Connection Planner](../../doc/controllers/intelligence-service-controller.md#status-connection-planner)


# Set Connection Planner

Retrieves available device windows for Connection Planner.

```python
def set_connection_planner(self,
                          body=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetDevicesWindowsRequestforplanner`](../../doc/models/get-devices-windows-requestforplanner.md) | Body, Optional | - |

## Response Type

**200**: The asynchronous request status.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AsynchronousRequestResultforplanner`](../../doc/models/asynchronous-request-resultforplanner.md).

## Example Usage

```python
body = GetDevicesWindowsRequestforplanner(
    account_number='0000123456-00001',
    filter='All or Best or Worst',
    devices=[
        DeviceListforplanner(
            device_ids=[
                DeviceIdforplanner(
                    kind='imei',
                    id='15-digit IMEI value'
                )
            ]
        )
    ]
)

result = intelligence_service_controller.set_connection_planner(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "d24cc6e4-eeee-ffff-gggg-0ffbb091c076"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 401 | Unauthorized | [`AuthRestErrorResponseforplannerException`](../../doc/models/auth-rest-error-responseforplanner-exception.md) |
| 403 | Forbidden | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 404 | Not Found / Does not exist | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 406 | Format / Request Unacceptable | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 429 | Too many requests | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| Default | Error response | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |


# Status Connection Planner

Retrieves the device status for the Connection Planner service.

```python
def status_connection_planner(self,
                             body=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetDeviceStatusesRequestforplanner`](../../doc/models/get-device-statuses-requestforplanner.md) | Body, Optional | - |

## Response Type

**200**: Success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetDeviceStatusesResponseforplanner`](../../doc/models/get-device-statuses-responseforplanner.md).

## Example Usage

```python
body = GetDeviceStatusesRequestforplanner(
    account_number='0000123456-00001',
    request_id='d24cc6e4-eeee-ffff-gggg-0ffbb091c076'
)

result = intelligence_service_controller.status_connection_planner(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "accountNumber": "0000123456-00001",
  "requestId": "d24cc6e4-eeee-ffff-gggg-0ffbb091c076",
  "deviceStatusList": [
    {
      "deviceIds": [
        {
          "kind": "Imei",
          "id": "15-digit IMEI"
        }
      ],
      "status": "SUCCESS",
      "reason": "reason for the status"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 401 | Unauthorized | [`AuthRestErrorResponseforplannerException`](../../doc/models/auth-rest-error-responseforplanner-exception.md) |
| 403 | Forbidden | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 404 | Not Found / Does not exist | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 406 | Format / Request Unacceptable | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| 429 | Too many requests | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |
| Default | Error response | [`RestErrorResponseforplannerException`](../../doc/models/rest-error-responseforplanner-exception.md) |

