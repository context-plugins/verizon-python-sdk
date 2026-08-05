# Account Service Controller

```python
account_service_controller = client.account_service_controller
```

## Class Name

`AccountServiceController`


# Get Account Information Using GET

Returns aaccount information associated with a specified account.

```python
def get_account_information_using_get(self,
                                     account_name)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | The account's numeric name, including leading zeroes. |

## Response Type

**200**: The account information related to an account.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetAccountInformationResponseforplanner`](../../doc/models/get-account-information-responseforplanner.md).

## Example Usage

```python
account_name = '0000123456-00002'

result = account_service_controller.get_account_information_using_get(account_name)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "string",
  "accountNumber": "0000123456-00001",
  "carriers": [
    "carrier name(s)"
  ],
  "features": [
    "feature names"
  ],
  "ipPools": [
    {
      "isDefaultPool": true,
      "poolName": "name of the pool",
      "poolType": "type of pool"
    }
  ],
  "isProvisioningAllowed": true,
  "organizationName": "Org Name",
  "servicePlans": [
    {
      "carrierServicePlanCode": "name of the service plan code",
      "code": "the activation code",
      "extendedAttributes": [
        {
          "key": "key name",
          "value": "key value"
        }
      ],
      "name": "name of the active profile carrier",
      "sizeKb": 1000
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

