# Hyper Precise Location Callbacks

```python
hyper_precise_location_callbacks_controller = client.hyper_precise_location_callbacks
```

## Class Name

`HyperPreciseLocationCallbacksController`

## Methods

* [List Registered Callbacks](../../doc/controllers/hyper-precise-location-callbacks.md#list-registered-callbacks)
* [Register Callback](../../doc/controllers/hyper-precise-location-callbacks.md#register-callback)
* [Deregister Callback](../../doc/controllers/hyper-precise-location-callbacks.md#deregister-callback)


# List Registered Callbacks

Find registered callback listener for account by account number.

```python
def list_registered_callbacks(self,
                             account_number)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Query, Required | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |

## Response Type

**200**: A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[CallbackCreated]`](../../doc/models/callback-created.md).

## Example Usage

```python
account_number = '0000123456-00001'

result = hyper_precise_location_callbacks_controller.list_registered_callbacks(account_number)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "0000123456-00001",
    "name": "BullseyeReporting",
    "url": "https://tsustgtests.mocklab.io/notifications/bullseye"
  }
]
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


# Register Callback

Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace Platform callback service. The messages are REST messages. You are responsible for creating and running a listening process on your server at that URL to receive and parse the messages.

```python
def register_callback(self,
                     account_number,
                     body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Query, Required | A unique identifier for an account. |
| `body` | [`HyperPreciseLocationCallback`](../../doc/models/hyper-precise-location-callback.md) | Body, Required | - |

## Response Type

**200**: A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CallbackRegistered`](../../doc/models/callback-registered.md).

## Example Usage

```python
account_number = '0000123456-00001'

body = HyperPreciseLocationCallback(
    name='BullseyeReporting',
    url='https://tsustgtests.mocklab.io/notifications/bullseye'
)

result = hyper_precise_location_callbacks_controller.register_callback(
    account_number,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "name": "BullseyeReporting"
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


# Deregister Callback

Stops ThingSpace from sending callback messages for the specified account and listener name.

```python
def deregister_callback(self,
                       account_number,
                       service)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Query, Required | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| `service` | `str` | Query, Required | The name of the callback service that will be deleted. |

## Response Type

**200**: Successful response (no content).

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
account_number = '0000123456-00001'

service = 'BullseyeReporting'

result = hyper_precise_location_callbacks_controller.deregister_callback(
    account_number,
    service
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

