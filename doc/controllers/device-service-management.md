# Device Service Management

```python
device_service_management_controller = client.device_service_management
```

## Class Name

`DeviceServiceManagementController`

## Methods

* [Get Device Hyper Precise Status](../../doc/controllers/device-service-management.md#get-device-hyper-precise-status)
* [Update Device Hyper Precise Status](../../doc/controllers/device-service-management.md#update-device-hyper-precise-status)


# Get Device Hyper Precise Status

Gets the list of a status for hyper-precise location devices.

```python
def get_device_hyper_precise_status(self,
                                   imei,
                                   account_number)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Query, Required | The International Mobile Equipment Identifier of the device. |
| `account_number` | `str` | Query, Required | The numeric name of the account and must include leading zeroes. |

## Response Type

**200**: Returns the status of Hyper Precise Location on the device.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BullseyeServiceResult`](../../doc/models/bullseye-service-result.md).

## Example Usage

```python
imei = '15-digit IMEI'

account_number = '0000123456-00001'

result = device_service_management_controller.get_device_hyper_precise_status(
    imei,
    account_number
)

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


# Update Device Hyper Precise Status

Enable/disable hyper-precise service for a device.

```python
def update_device_hyper_precise_status(self,
                                      body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BullseyeServiceRequest`](../../doc/models/bullseye-service-request.md) | Body, Required | List of devices and hyper-precise required statuses. |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BullseyeServiceResult`](../../doc/models/bullseye-service-result.md).

## Example Usage

```python
body = BullseyeServiceRequest(
    device_list=[
        DeviceServiceRequest(
            imei='15-digit IMEI',
            bullseye_enable=HplBullseyeEnable(
                bullseye_enable=True
            )
        )
    ],
    account_number='0000123456-00001'
)

result = device_service_management_controller.update_device_hyper_precise_status(body)

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

