# Device Credential Management

```python
device_credential_management_controller = client.device_credential_management
```

## Class Name

`DeviceCredentialManagementController`

## Methods

* [Retrieve Credentials](../../doc/controllers/device-credential-management.md#retrieve-credentials)
* [Generate Credentials](../../doc/controllers/device-credential-management.md#generate-credentials)
* [Reset Credentials](../../doc/controllers/device-credential-management.md#reset-credentials)
* [Drop Credentials](../../doc/controllers/device-credential-management.md#drop-credentials)


# Retrieve Credentials

```python
def retrieve_credentials(self,
                        body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CredentialsRequest`](../../doc/models/credentials-request.md) | Body, Required | - |

## Response Type

**200**: Successful retrieval

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RetrieveResponse`](../../doc/models/retrieve-response.md).

## Example Usage

```python
body = CredentialsRequest(
    ecpd='3161585',
    account_number='0844021539-00001',
    items=[
        DeviceCredentialRequestItem(
            imei='221000008775573'
        )
    ]
)

result = device_credential_management_controller.retrieve_credentials(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request / Verification Failure | [`ErrorResponseException`](../../doc/models/error-response-exception.md) |
| 401 | Unauthorized | `APIException` |


# Generate Credentials

```python
def generate_credentials(self,
                        body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CredentialsRequest`](../../doc/models/credentials-request.md) | Body, Required | - |

## Response Type

**200**: Credentials generated successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GenerateResponse`](../../doc/models/generate-response.md).

## Example Usage

```python
body = CredentialsRequest(
    ecpd='3161585',
    account_number='0844021539-00001',
    items=[
        DeviceCredentialRequestItem(
            imei='221000008775573'
        )
    ]
)

result = device_credential_management_controller.generate_credentials(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseException`](../../doc/models/error-response-exception.md) |


# Reset Credentials

```python
def reset_credentials(self,
                     body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CredentialsRequest`](../../doc/models/credentials-request.md) | Body, Required | - |

## Response Type

**200**: Credentials reset successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GenerateResponse`](../../doc/models/generate-response.md).

## Example Usage

```python
body = CredentialsRequest(
    ecpd='3161585',
    account_number='0844021539-00001',
    items=[
        DeviceCredentialRequestItem(
            imei='221000008775573'
        )
    ]
)

result = device_credential_management_controller.reset_credentials(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseException`](../../doc/models/error-response-exception.md) |


# Drop Credentials

```python
def drop_credentials(self,
                    body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CredentialsRequest`](../../doc/models/credentials-request.md) | Body, Required | - |

## Response Type

**200**: Credentials dropped successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DropResponse`](../../doc/models/drop-response.md).

## Example Usage

```python
body = CredentialsRequest(
    ecpd='3161585',
    account_number='0844021539-00001',
    items=[
        DeviceCredentialRequestItem(
            imei='221000008775573'
        )
    ]
)

result = device_credential_management_controller.drop_credentials(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseException`](../../doc/models/error-response-exception.md) |

