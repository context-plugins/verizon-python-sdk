# Exclusions

Exclude devices from location services.

```python
exclusions_controller = client.exclusions
```

## Class Name

`ExclusionsController`

## Methods

* [Devices Location Get Consent Async](../../doc/controllers/exclusions.md#devices-location-get-consent-async)
* [Devices Location Give Consent Async](../../doc/controllers/exclusions.md#devices-location-give-consent-async)
* [Devices Location Update Consent](../../doc/controllers/exclusions.md#devices-location-update-consent)
* [Exclude Devices](../../doc/controllers/exclusions.md#exclude-devices)
* [Remove Devices from Exclusion List](../../doc/controllers/exclusions.md#remove-devices-from-exclusion-list)
* [List Excluded Devices](../../doc/controllers/exclusions.md#list-excluded-devices)


# Devices Location Get Consent Async

Get the consent settings for the entire account or device list in an account.

```python
def devices_location_get_consent_async(self,
                                      account_name,
                                      device_id=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | The numeric name of the account. |
| `device_id` | `str` | Query, Optional | The IMEI of the device being queried |

## Response Type

**200**: List of JSON objects, each containing the position data or an error for a device in the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetAccountDeviceConsent`](../../doc/models/get-account-device-consent.md).

## Example Usage

```python
account_name = '0000123456-00001'

device_id = '900000000000009'

result = exclusions_controller.devices_location_get_consent_async(
    account_name,
    device_id=device_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Devices Location Give Consent Async

Create a consent record to use location services as an asynchronous request.

```python
def devices_location_give_consent_async(self,
                                       body=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountConsentCreate`](../../doc/models/account-consent-create.md) | Body, Optional | Account details to create a consent record. |

## Response Type

**200**: List of JSON objects, each containing the position data or an error for a device in the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConsentTransactionID`](../../doc/models/consent-transaction-id.md).

## Example Usage

```python
body = AccountConsentCreate(
    account_name='0000123456-00001'
)

result = exclusions_controller.devices_location_give_consent_async(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Devices Location Update Consent

Update the location services consent record for an entire account.

```python
def devices_location_update_consent(self,
                                   body=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountConsentUpdate`](../../doc/models/account-consent-update.md) | Body, Optional | Account details to update a consent record. |

## Response Type

**200**: List of JSON objects, each containing the position data or an error for a device in the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConsentTransactionID`](../../doc/models/consent-transaction-id.md).

## Example Usage

```python
body = AccountConsentUpdate(
    account_name='0000123456-00001',
    all_device_consent=0
)

result = exclusions_controller.devices_location_update_consent(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Exclude Devices

This consents endpoint sets a new exclusion list.

```python
def exclude_devices(self,
                   body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConsentRequest`](../../doc/models/consent-request.md) | Body, Required | Request to update account consent exclusion list. |

## Response Type

**200**: Success response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
body = ConsentRequest(
    account_name='1234567890-00001',
    all_device=False,
    mtype='replace',
    exclusion=[
        '980003420535573',
        '375535024300089',
        'A100003861E585'
    ]
)

result = exclusions_controller.exclude_devices(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Remove Devices from Exclusion List

Removes devices from the exclusion list so that they can be located with Device Location Services requests.

```python
def remove_devices_from_exclusion_list(self,
                                      account_name,
                                      device_list)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | The numeric name of the account. |
| `device_list` | `str` | Query, Required | A list of the device IDs to remove from the exclusion list. |

## Response Type

**200**: Devices successfully removed from list.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
account_name = '0000123456-00001'

device_list = 'IMEI'

result = exclusions_controller.remove_devices_from_exclusion_list(
    account_name,
    device_list
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# List Excluded Devices

This consents endpoint retrieves a list of excluded devices in an account.

```python
def list_excluded_devices(self,
                         account_name,
                         start_index)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Account identifier in "##########-#####". |
| `start_index` | `str` | Template, Required | Zero-based number of the first record to return. |

## Response Type

**200**: Excluded devices result.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DevicesConsentResult`](../../doc/models/devices-consent-result.md).

## Example Usage

```python
account_name = '0252012345-00001'

start_index = '0'

result = exclusions_controller.list_excluded_devices(
    account_name,
    start_index
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "2024009649-00001",
  "allDevice": false,
  "hasMoreData": false,
  "totalCount": 4,
  "updateTime": "2018-05-18 19:20:50.076 +0000 UTC",
  "exclusion": [
    "990003420535375",
    "420535399000375",
    "A100003861E585",
    "205353759900034"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

