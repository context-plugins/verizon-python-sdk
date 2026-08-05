# Device-Role-Controller

```python
device_role_controller = client.device_role_controller
```

## Class Name

`DeviceRoleController`


# Get ACL Rules by Vendor Id

This API allows the user to get the access control rules defined for them.

```python
def get_acl_rules_by_vendor_id(self,
                              vendor_id)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [sessionToken](../../doc/auth/custom-header-signature-1.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Query, Required | The user's Vendor ID<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9]+$` |

## Response Type

**200**: List of Access Rules

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DeviceRole]`](../../doc/models/device-role.md).

## Example Usage

```python
vendor_id = 'TestVendor'

result = device_role_controller.get_acl_rules_by_vendor_id(vendor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 406 | Not Acceptable | `APIException` |
| 429 | Too many requests | `APIException` |
| Default | unexpected error | `APIException` |

